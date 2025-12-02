from dash import Input,Output
import dash
from sl2_dash.components.ids import Nav

def register_info_instructions_callback(app:dash.Dash)-> None:

    @app.callback(Output('instructions_modal','is_open'),
                  Input(Nav.INSTRUCTIONS,'n_clicks'),
                  prevent_initial_call=True)
    def _open_instructions(_):
        return True
    
    @app.callback(Output('info_modal','is_open'),
                  Input(Nav.INFO,'n_clicks'),
                  prevent_initial_call=True)
    def _open_info(_):
        return True
    


