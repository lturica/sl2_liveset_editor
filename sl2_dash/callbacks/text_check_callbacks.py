from sl2_dash.components.ids import GlobalSettings

import dash
from dash import Input,Output


# Function to validate the names for the Liveset and Patch.

def register_text_check_callbacks(app: dash.Dash) -> None:
    """Register sl2_dash.callbacks to validate text inputs for liveset and patch names."""
    @app.callback([Output(GlobalSettings.LIVE_SET_NAME, "valid"), Output(GlobalSettings.LIVE_SET_NAME, "invalid")],
                Input(GlobalSettings.LIVE_SET_NAME, "value"))
    def validate_liveset_name(name):
        context = dash.callback_context
        if context.triggered_id is None:
            return dash.no_update
        valid = name.isascii() and (len(name)>0) 
        return valid, not valid


    @app.callback([Output(GlobalSettings.PATCH_NAME, "valid"), Output(GlobalSettings.PATCH_NAME, "invalid")],
                Input(GlobalSettings.PATCH_NAME, "value"))
    def validate_patch_name(name):
        context = dash.callback_context
        if context.triggered_id is None:
            return dash.no_update
        valid = name.isascii() and (len(name)>0) and (len(name)<17)
        return valid, not valid
    

