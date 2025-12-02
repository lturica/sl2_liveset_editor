import io
import dash
from dash import Input, Output, no_update
from sl2_dash.components.ids import Nav
import importlib.resources as resources
from typing import List


# this file contains the code to choose and load default .tsl files from the 'res' directory.
# A modal is used, with a dropdown populated with the available .tsl files.
# the modal is triggered by clicking the "Choose Default" nav link in the header navbar.
# Loading is done by clicking the "Load" button in the modal. The logic requests an 'upload' of the selected file.


def list_tsl_files() -> List[str]:
    """
    Return list of '.tsl' filenames inside the 'res' package.
    Uses importlib.resources (py3.9+) and falls back to filesystem if needed.
    """
    try:
        pkg_root = resources.files("res")
        return [
            p.name
            for p in pkg_root.iterdir()
            if p.is_file() and p.suffix.lower() == ".tsl"
        ]
    except Exception as e:
        raise RuntimeError("Failed to list .tsl files from 'res' package") from e


def read_tsl_file(filename: str) -> bytes:
    """
    Read the contents of a .tsl file from the 'res' package.
    Returns the file contents as bytes.
    """
    with resources.as_file(resources.files("res") / filename) as file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            return io.StringIO(f.read())


def register_choose_default_callbacks(app: dash.Dash) -> None:
    """Register sl2_dash.callbacks for the choose-default modal (open + load closing handled together)."""

    @app.callback(
        Output("choose-default-modal", "is_open"),
        Output(Nav.DEFAULT_DROPDOWN, "options"),
        Output(Nav.DEFAULT_DROPDOWN, "value"),
        Input(Nav.DEFAULT_CHOICE, "n_clicks"),  # navbar clicked
        Input(Nav.LOAD_DEFAULT_BUTTON, "n_clicks"),  # load default button clicked
        prevent_initial_call=True,
    )
    def open_handle_modal(open_click, load_click):
        ctx = dash.callback_context
        if ctx.triggered_id is None:
            return no_update
        elif ctx.triggered_id == Nav.LOAD_DEFAULT_BUTTON:
            # close modal when button is pressed
            return False, no_update, no_update
        elif ctx.triggered_id == Nav.DEFAULT_CHOICE:
            # Open modal and populate dropdown options
            files = list_tsl_files()
            options = [{"label": f, "value": f} for f in files]
            return True, options, files[0]
