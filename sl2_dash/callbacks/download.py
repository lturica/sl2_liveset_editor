import json
import io
import base64

import sl2
from sl2_dash.components.ids import JSON_STORE, CURRENT_PATCH_ID, Toast, Nav
from .helpers import ui_to_liveset

import dash
import dash_bootstrap_components as dbc
import numpy as np
from dash import html, dcc, Output, Input, State

from sl2_dash.config.ui_mapping import ALL_STATES


def register_download_callback(app: dash.Dash):
    @app.callback(
        Output(Nav.DOWNLOAD, "data"),
        Input(Nav.DOWNLOAD_BUTTON, "n_clicks"),
        State(JSON_STORE, "data"),
        State(CURRENT_PATCH_ID, "data"),
        *[ALL_STATES[i] for i in range(len(ALL_STATES))],  # all global + slicer states
        prevent_initial_call=True,
    )
    def _handle_download(n_clicks, json_str, current_patch_id, *state_values):
        ctx = dash.callback_context
        if not ctx.triggered_id:
            return dash.no_update

        # Build the updated LiveSet
        live_set = ui_to_liveset(
            json_str, list(state_values), patch_id=current_patch_id
        )

        # Convert to JSON string
        out_json = json.dumps(live_set.dict(), separators=(",", ":"))

        # Use LiveSet name for filename
        filename = f"{live_set.name}.tsl"

        # print(f"Downloading {filename}")
        return dict(content=out_json, filename=filename)
