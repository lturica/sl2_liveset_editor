import dash_bootstrap_components as dbc

from .ids import Toast


######################
# Toast Declarations #
######################

# Global registries
ALL_TOASTS = []


def register_toast(obj):
    """Decorator that registers a Toast in the ALL_TOASTS list."""
    ALL_TOASTS.append(obj)
    return obj


# Error toast is displayed when a file upload fails for some reason

err_toast = register_toast(
    dbc.Toast(
        "Unable to parse .tsl file!",
        id=Toast.LOAD_ERROR,
        header="File Error",
        is_open=False,
        dismissable=True,
        duration=3000,
        icon="danger",
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 999,
        },
    )
)

# Success toast is displayed when a file upload is successful, to let the user know that their file has been uploaded.
success_toast = register_toast(
    dbc.Toast(
        "Loaded .tsl file sucessfully!",
        id=Toast.LOAD_SUCCESS,
        header="File Upload Successful",
        is_open=False,
        dismissable=True,
        duration=3000,
        icon="success",
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 999,
        },
    )
)

# patch delete, selected, and duplicated appear within the liveset
patch_delete_toast = register_toast(
    dbc.Toast(
        "Deleted patch!",
        id=Toast.PATCH_DELETE,
        header="Patch Deletion Successful",
        is_open=False,
        dismissable=True,
        duration=3000,
        icon="warning",
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 999,
        },
    )
)

patch_selected_toast = register_toast(
    dbc.Toast(
        "Selected patch!",
        id=Toast.PATCH_SELECT,
        header="Patch Selection Successful",
        is_open=False,
        dismissable=True,
        duration=3000,
        icon="info",
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 999,
        },
    )
)

patch_duplicated_toast = register_toast(
    dbc.Toast(
        "Duplicated patch!",
        id=Toast.PATCH_DUPLICATE,
        header="Patch Duplication Successful",
        is_open=False,
        dismissable=True,
        duration=3000,
        icon="info",
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 999,
        },
    )
)

patch_delete_fail_toast = register_toast(
    dbc.Toast(
        "Unable to delete patch!",
        id=Toast.PATCH_CANNOT_DELETE,
        header="Cannot Delete The Only Patch",
        is_open=False,
        dismissable=True,
        duration=3000,
        icon="danger",
        style={
            "position": "fixed",
            "top": 66,
            "right": 10,
            "width": 350,
            "zIndex": 999,
        },
    )
)
