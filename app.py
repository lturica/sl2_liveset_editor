
import dash
import dash_bootstrap_components as dbc

# Layout components
from sl2_dash.components.header_navbar import header_navbar
from sl2_dash.components.body_layout import body
from sl2_dash.components.store_locations import stores

# Callbacks
from sl2_dash.callbacks.text_check_callbacks import register_text_check_callbacks
from sl2_dash.callbacks.info_instructions import register_info_instructions_callback
from sl2_dash.callbacks.choose_default_tsl_files import register_choose_default_callbacks
from sl2_dash.callbacks.upload import register_upload_callback
from sl2_dash.callbacks.download import register_download_callback
from sl2_dash.callbacks.patch_del_select_copy import register_patch_modify_callbacks
from sl2_dash.callbacks.disable_sliders import register_disable_slicer_channels_callback
from sl2_dash.callbacks.duplicate_c1_to_c2 import register_copy_c1_c2_button_callbacks
from sl2_dash.callbacks.help_tooltips import register_tooltip_modals


# Main Plotly Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE, dbc.icons.BOOTSTRAP],)
app.title = "SL-2 Live Set Editor"

# App Layout 

app.layout = dash.html.Div([*stores, header_navbar, body])

# Callbacks

register_text_check_callbacks(app)
register_info_instructions_callback(app)
register_choose_default_callbacks(app)
register_upload_callback(app)
register_download_callback(app)
register_patch_modify_callbacks(app)
register_disable_slicer_channels_callback(app)
register_copy_c1_c2_button_callbacks(app)
register_tooltip_modals(app)


# Local Server
if __name__ == "__main__":
    app.run(debug=False)


