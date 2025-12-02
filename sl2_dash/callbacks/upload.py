import json
import io
import base64

import sl2
from sl2_dash.components.ids import JSON_STORE, CURRENT_PATCH_ID, Toast, Nav
from .helpers import liveset_to_ui_outputs
from sl2_dash.config.ui_mapping import ALL_OUTPUTS, ALL_OUTPUTS_LEN
from sl2_dash.callbacks.choose_default_tsl_files import read_tsl_file


import dash
import dash_bootstrap_components as dbc
import numpy as np
from dash import html, dcc, Output, Input, State


def register_upload_callback(
    app: dash.Dash,
):
    @app.callback(
        ALL_OUTPUTS
        + [
            Output(JSON_STORE, "data", allow_duplicate=True),
            Output(Toast.LOAD_ERROR, "is_open"),
            Output(Toast.LOAD_SUCCESS, "is_open", allow_duplicate=True),
            Output(
                CURRENT_PATCH_ID, "data", allow_duplicate=True
            ),  # set the current patch to first one when upload is successful
        ],
        Input(Nav.UPLOAD, "contents"),
        Input(Nav.LOAD_DEFAULT_BUTTON, "n_clicks"),  # load default button clicked
        State(Nav.DEFAULT_DROPDOWN, "value"),
        prevent_initial_call=True,
    )
    def _upload_and_update_ui(contents, n_default_clicks: int, default_tsl_name: str):
        show_success = False
        show_err = False
        current_patch_id = dash.no_update
        ctx = dash.callback_context
        if ctx.triggered_id is None:
            return [dash.no_update] * ALL_OUTPUTS_LEN + [
                dash.no_update,
                show_err,
                show_success,
                current_patch_id,
            ]

        # --- LOAD LIVESET FROM DEFAULTS ---
        elif ctx.triggered_id == Nav.LOAD_DEFAULT_BUTTON:
            # Load the selected DEFAULT .tsl file
            if default_tsl_name is None:
                # print("No default .tsl file selected.")
                show_err = True
                return [dash.no_update] * ALL_OUTPUTS_LEN + [
                    dash.no_update,
                    show_err,
                    show_success,
                    current_patch_id,
                ]
            try:
                # test encode to sl2 and generate json data for store
                live_set = sl2.read_tsl(read_tsl_file(default_tsl_name))
                json_data = json.dumps(live_set.dict(), separators=(",", ":"))
                show_success = True
                current_patch_id = 0
                # Convert to UI outputs
                ui_values = liveset_to_ui_outputs(live_set)
                return (*ui_values, json_data, show_err, show_success, current_patch_id)
            except Exception as e:
                # print(f"Error loading default .tsl file '{default_tsl_name}':", e)
                show_err = True
                return [dash.no_update] * ALL_OUTPUTS_LEN + [
                    dash.no_update,
                    show_err,
                    show_success,
                    current_patch_id,
                ]

        # --- UPLOAD LIVESET FROM USER ---
        elif ctx.triggered_id == Nav.UPLOAD:
            try:
                _, cstr = contents.split(",", maxsplit=1)
                bstr = base64.b64decode(cstr)
                buf = io.StringIO(bstr.decode("utf-8"))
                live_set = sl2.read_tsl(buf)

                json_data = json.dumps(live_set.dict(), separators=(",", ":"))
                show_success = True
                current_patch_id = 0
                # Convert to UI outputs
                ui_values = liveset_to_ui_outputs(live_set)

                return (*ui_values, json_data, show_err, show_success, current_patch_id)
            except Exception as e:
                # print("Error parsing .tsl:", e)
                show_err = True
                return [dash.no_update] * ALL_OUTPUTS_LEN + [
                    dash.no_update,
                    show_err,
                    show_success,
                    current_patch_id,
                ]
