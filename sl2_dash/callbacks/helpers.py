
import io

import sl2 
from sl2_dash.config.ui_mapping import GROUP_LENGTHS



def liveset_to_ui_outputs(live_set: sl2.LiveSet,patch_id: int=0) -> list:
    # patch_id is by default 0, the first patch
    # when select a different patch, this needs to be updated accordingly
    
    try:
        params = live_set.data[0][patch_id].paramSet  # adjust if structure changes
        memo = live_set.data[0][patch_id].memo.memo
    except Exception as e:
        #print(f" Error accessing patch {patch_id} in liveset: {e}")
        #print(f" Defaulting to patch 0")
        params = live_set.data[0][0].paramSet  # fallback to 0th param set
        memo = live_set.data[0][0].memo.memo
    return [
        live_set.name,                      # GlobalSettings.LIVE_SET_NAME
        params.com.string,                  # GlobalSettings.PATCH_NAME  
        live_set.device,                    # GlobalSettings.LIVE_SET_DEVICE
        live_set.formatRev,                 # GlobalSettings.LIVE_SET_FORMAT_REV
        memo,
        *params.slicer_1.to_db_list(),      # slicer channel 1 sliders
        *params.slicer_2.to_db_list(),      # slicer channel 2 sliders
        *params.phaser_1.to_db_list(),
        *params.phaser_2.to_db_list(),
        *params.flanger_1.to_db_list(),
        *params.flanger_2.to_db_list(),
        *params.tremolo_1.to_db_list(),
        *params.tremolo_2.to_db_list(),
        *params.overtone_1.to_db_list(),
        *params.overtone_2.to_db_list(),
        *params.beat.to_db_list(),
        *params.comp.to_db_list(),
        *params.divider.to_db_list(),
        *params.mixer.to_db_list(),
        *params.ns.to_db_list(),
        *params.peq.to_db_list(),
    ]


def ui_to_liveset(json_str: str,param_array: list[list], patch_id:int=0, ) -> sl2.LiveSet:
    """Update a LiveSet from UI state values in the same order as ALL_STATES."""
    
    # Step 1: load base liveset from JSON_STORE
    if json_str:
        live_set = sl2.read_tsl(io.StringIO(json_str))
    else:
        # or make a default liveset if none is given
        params = sl2.ParamSet()
        patch = sl2.Patch(paramSet=params)
        live_set = sl2.LiveSet(name="New Live Set", formatRev="0001",device= "SL-2",data= [[patch]])
        patch_id = 0 # reset to patch id 0
    
    # split param array into param groups
    param_groups = [param_array[sum(GROUP_LENGTHS[:i]):sum(GROUP_LENGTHS[:i+1])] for i in range(len(GROUP_LENGTHS))]
    patch = live_set.data[0][patch_id]
    params = patch.paramSet

    # globals
    global_vals = param_groups[0]

    live_set.name = global_vals[0] # liveset name
    params.com.string = global_vals[1] # patch name
    # these 3 cannot be changed using the ui
    live_set.device = global_vals[2]
    live_set.formatRev = global_vals[3]
    patch.memo.memo = global_vals[4] if len(global_vals) > 4 else patch.memo.memo 

    #  update all modules
    params.slicer_1 =   [int(x) for x in param_groups[1]]
    params.slicer_2 =   [int(x) for x in param_groups[2]]
    params.phaser_1 =   [int(x) for x in param_groups[3]]
    params.phaser_2 =   [int(x) for x in param_groups[4]]
    params.flanger_1 =  [int(x) for x in param_groups[5]]
    params.flanger_2 =  [int(x) for x in param_groups[6]]
    params.tremolo_1 =  [int(x) for x in param_groups[7]]
    params.tremolo_2 =  [int(x) for x in param_groups[8]]
    params.overtone_1 = [int(x) for x in param_groups[9]]
    params.overtone_2 = [int(x) for x in param_groups[10]]
    params.beat =       [int(x) for x in param_groups[11]]
    params.comp =       [int(x) for x in param_groups[12]]
    params.divider =    [int(x) for x in param_groups[13]]
    params.mixer =      [int(x) for x in param_groups[14]]
    params.ns =         [int(x) for x in param_groups[15]]
    params.peq =        [int(x) for x in param_groups[16]]

    return live_set