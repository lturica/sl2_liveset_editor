
import io
import json
import copy

from sl2_dash.components.ids import GlobalSettings,Toast,JSON_STORE,CURRENT_PATCH_ID
import sl2
from .helpers import liveset_to_ui_outputs,ui_to_liveset
from sl2_dash.config.ui_mapping import ALL_OUTPUTS,ALL_OUTPUTS_LEN,ALL_STATES

import dash
from dash import Output, Input, State




def register_patch_modify_callbacks(app:dash.Dash):

    # open and close the confirm delete modal when the buttons are clicked
    @app.callback(Output(GlobalSettings.CONFIRM_DELETE_MODAL,'is_open',allow_duplicate=True),
                Input(GlobalSettings.PATCH_DELETE_BUTTON,'n_clicks'),
                prevent_initial_call=True,)
    def _open_delete_confirm_modal(n_clicks:int):
        return True
    @app.callback(Output(GlobalSettings.CONFIRM_DELETE_MODAL,'is_open',allow_duplicate=True),
                Input(GlobalSettings.CONFIRM_DELETE_BUTTON,'n_clicks'),
                prevent_initial_call=True,)
    def _close_delete_confirm_modal(n_clicks:int):
        return False
    
    # update the patch delete list when the json storage data is changed
    @app.callback(Output(GlobalSettings.PATCH_SELECT_DROPDOWN,'options',allow_duplicate=True),
                Input(JSON_STORE,'data'),
                prevent_initial_call=True
                )
    def _generate_patch_select_list(json_str:str):
        # generate list of patches available in the current tsl file
        # triggers whenever tsl file is changed
        patch_names = sl2.read_tsl(io.StringIO(json_str)).patchNames
        return [{"label": patchName, "value": i} for i, patchName in enumerate (patch_names)]
    



    @app.callback(
        *ALL_OUTPUTS,
        Output(JSON_STORE, "data", allow_duplicate=True),
        Output(CURRENT_PATCH_ID, "data", allow_duplicate=True),
        Output(GlobalSettings.PATCH_SELECT_DROPDOWN, "value", allow_duplicate=True),
        Output(Toast.PATCH_SELECT,'is_open'),           # patch select toast
        Output(Toast.PATCH_DUPLICATE,'is_open'),        # patch duplicate toast
        Output(Toast.PATCH_DELETE,'is_open'),           # patch delete toast
        Output(Toast.PATCH_CANNOT_DELETE,'is_open'),    # patch delete error toast
        #Input(GlobalSettings.PATCH_SELECT_BUTTON, "n_clicks"),          # Load button
        Input(GlobalSettings.PATCH_SELECT_DROPDOWN, "value"),          # Load button
        Input(GlobalSettings.PATCH_DUPLICATE_BUTTON, "n_clicks"),       # Duplicate button
        Input(GlobalSettings.CONFIRM_DELETE_BUTTON, "n_clicks"),          # Delete button
        State(JSON_STORE, "data"),
        State(CURRENT_PATCH_ID, "data"),
        #State(GlobalSettings.PATCH_SELECT_DROPDOWN, "value"),
        *[ALL_STATES[i] for i in range(len(ALL_STATES))],               # all UI states
        prevent_initial_call=True,
    )
    def _handle_patch_buttons(n_load, n_copy:int, n_delete:int,
                            json_str:str, current_patch_id:int, #dropdown_value:int,
                            *state_values):
        

        #dropdown_value = int(dropdown_value)
        dropdown_value = n_load = int(n_load)
        current_patch_id = int(current_patch_id)

        select_toast, duplicate_toast, delete_toast, cannot_delete_toast=False, False, False, False
        ctx = dash.callback_context
        if not ctx.triggered_id or not json_str:
            return [dash.no_update] * ALL_OUTPUTS_LEN + [dash.no_update, dash.no_update, dash.no_update, 
                                                        select_toast, duplicate_toast, delete_toast, cannot_delete_toast]

        live_set = sl2.read_tsl(io.StringIO(json_str))
        total_patches = len(live_set.data[0])
        trig = ctx.triggered_id

        # --- SELECT PATCH ---
        if trig == GlobalSettings.PATCH_SELECT_DROPDOWN:
            live_set = ui_to_liveset(json_str, list(state_values), patch_id=current_patch_id) # save current patch
            new_patch_id = dropdown_value
            ui_values = liveset_to_ui_outputs(live_set, patch_id=new_patch_id) # load new patch to ui
            new_json = json.dumps(live_set.dict(), separators=(",", ":")) # json encode liveset
            select_toast = True
            #print('Selected patch.')
            return (*ui_values, new_json, new_patch_id, new_patch_id, 
                    select_toast, duplicate_toast, delete_toast, cannot_delete_toast)

        # --- DUPLICATE PATCH ---
        elif trig == GlobalSettings.PATCH_DUPLICATE_BUTTON:
            live_set = ui_to_liveset(json_str, list(state_values), patch_id=current_patch_id)
            new_patch = copy.deepcopy(live_set.data[0][current_patch_id])
            live_set.data[0].append(new_patch) # add new patch to liveset
            live_set.data[0][-1].paramSet.com.string = live_set.data[0][-1].paramSet.com.string[:12]+'COPY' # remove the last bits of the string and replace name with cpy
            live_set.data[0][-1].paramSet._storage["PATCH%COM"] = live_set.data[0][-1].paramSet.com 
            # deepcopy desyncs this. In reality one should have the _storage and paramArrays identical or fetch the dict from the live view
            new_patch_id = len(live_set.data[0]) - 1 # focus on new patch
            ui_values = liveset_to_ui_outputs(live_set, patch_id=new_patch_id) # load new patch to ui
            new_json = json.dumps(live_set.dict(), separators=(",", ":")) # json encode liveset
            duplicate_toast = True
            #print('Duplicated patch.')
            return (*ui_values, new_json, new_patch_id, new_patch_id, 
                    select_toast, duplicate_toast, delete_toast, cannot_delete_toast)

        # --- DELETE PATCH ---
        elif trig == GlobalSettings.CONFIRM_DELETE_BUTTON:
            if total_patches <= 1:
                #print("Cannot delete the only patch in the LiveSet.")
                cannot_delete_toast = True
                return [dash.no_update] * ALL_OUTPUTS_LEN + [dash.no_update, dash.no_update, dash.no_update, 
                                                            select_toast, duplicate_toast, delete_toast, cannot_delete_toast]
            live_set.data[0].pop(current_patch_id)
            new_patch_id = '0' # switch to patch 0 
            ui_values = liveset_to_ui_outputs(live_set, patch_id=new_patch_id) # load new patch to ui
            new_json = json.dumps(live_set.dict(), separators=(",", ":")) # json encode liveset
            delete_toast = True
            #print('Deleted patch.')
            return (*ui_values, new_json, new_patch_id, new_patch_id,select_toast, 
                    duplicate_toast, delete_toast, cannot_delete_toast)
        
        return [dash.no_update] * ALL_OUTPUTS_LEN + [dash.no_update, dash.no_update, dash.no_update, 
                                                    select_toast, duplicate_toast, delete_toast, cannot_delete_toast]

