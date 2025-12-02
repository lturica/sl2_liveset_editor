


# ids for varioussl2_dash.components in the app


JSON_STORE = "json-store"
CURRENT_PATCH_ID = 'current-patch-id-store'

### navbar
class Nav:
    HEADER = "nav-header"
    UPLOAD = "upload"
    DOWNLOAD_BUTTON = "download_button"
    DOWNLOAD = "download"
    DEFAULT_CHOICE = "default_choice"
    LOAD_DEFAULT_BUTTON = "load-default-button"
    DEFAULT_DROPDOWN = "default-tsl-dropdown"
    INFO = 'info-navbar'
    INSTRUCTIONS = 'instructions-navbar'
    

### cards
class Debug:
    DEBUG_CARD = "debug-card"
    DEBUG_TEXT_1 = "debug-card-pre-1"
    DEBUG_TEXT_2 = "debug-card-pre-2"
    DEBUG_TEXT_3 = "debug-card-pre-3"
    DEBUG_TEXT_4 = "debug-card-pre-4"

class GlobalSettings:
    LIVE_SET_NAME = "ls_name"
    LIVE_SET_DEVICE = "ls_device"
    LIVE_SET_FORMAT_REV = "ls_format_rev"
    PATCH_NAME = "patch_name"
    MEMO='patch_memo'
    # the above are parameters
    # the below are operational ids
    PATCH_SELECT_DROPDOWN = 'patch_select_dropdown'
    PATCH_SELECT_BUTTON = 'patch_select_button'
    PATCH_DUPLICATE_BUTTON = 'patch_duplicate_button'
    PATCH_DELETE_BUTTON = 'patch_delete_button'
    CONFIRM_DELETE_MODAL = 'confirm-delete-modal'
    CONFIRM_DELETE_BUTTON = 'confirm-delete-button'

    def global_list():
        return [GlobalSettings.LIVE_SET_NAME,
                GlobalSettings.PATCH_NAME,
                GlobalSettings.LIVE_SET_DEVICE,
                GlobalSettings.LIVE_SET_FORMAT_REV,
                GlobalSettings.MEMO
                ]
    

class ChannelCopy:
    SLICER = {"step_length": 'slicer_length_channel_copy_button',
              "step_level": 'slicer_step_level_channel_copy_button',
              "band_pass": 'slicer_band_pass_channel_copy_button',
              "effect_level": "slicer_fx_level_channel_copy_button",
              "pitch_shift": "slicer_pitch_channel_copy_button",}
    PHASER = 'phaser_channel_copy_button'
    FLANGER = 'flanger_channel_copy_button'
    TREMOLO = 'tremolo_channel_copy_button'
    OVERTONE = 'overtone_channel_copy_button'
    DOUBLE_CLICK_TIMESTAMP = 'double_click_timestamp_store'

### TOASTS
class Toast:
    LOAD_ERROR = "err_toast"
    LOAD_SUCCESS = "success_toast"
    PATCH_DELETE = "patch_delete_toast" 
    PATCH_SELECT = "patch_select_toast" 
    PATCH_DUPLICATE = "patch_duplicate_toast"
    PATCH_CANNOT_DELETE = 'patch_delet_err_toast'


