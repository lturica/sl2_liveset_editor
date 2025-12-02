import numpy as np
import dash
from dash import Input, Output


from sl2.params import slicer
from sl2_dash.components.cards.slicer import N_SLIDER_GROUPS, N_CHANNELS
from sl2_dash.components.cards.slicer import (
    slicer_c1_slider_ids,
    slicer_c2_slider_ids,
)  # change to move directly to cards


# Function to set which sliders are disabled based on
# the channel enable flag, the step number, and the pattern flag
def disable_channels(enable, step_num, pattern, effect):
    # Step number flag
    step_num = int(step_num)
    step_num_flag = np.full(N_CHANNELS, False)
    for v in slicer.STEP_NUMBER:
        if step_num == v.value:
            d_val = int(v.name.replace("STEP_", ""))
            step_num_flag = np.array([False] * d_val + [True] * (N_CHANNELS - d_val))
            break
    # Pattern flag works just like enable
    pattern = int(pattern)
    pattern_flag = pattern != 50
    # Check if effect is set to anything other than pitch.
    effect = int(effect)
    # If so, we need to disable all pitch_shift sliders.
    if effect != slicer.FX_TYPE.PITCH:
        pitch_flag = np.array(
            [
                elem["id"].startswith("pitch_shift")
                for elem in dash.callback_context.outputs_list
            ]
        )
    else:
        pitch_flag = False
    return (
        np.tile(step_num_flag, N_SLIDER_GROUPS)
        | (not enable)
        | pitch_flag
        | pattern_flag
    ).tolist()


def register_disable_slicer_channels_callback(app: dash.Dash) -> None:
    # Callback to disable the appropriate sliders depending on user's settings.
    @app.callback(
        *(Output(c1_t, "disabled") for c1_t in slicer_c1_slider_ids),
        Input("slicer_c1_enable", "value"),
        Input("slicer_c1_step_num", "value"),
        Input("slicer_c1_pattern", "value"),
        Input("slicer_c1_effect", "value"),
    )
    def _dis_c1_channels(enable, step_num, pattern, effect):
        return disable_channels(enable, step_num, pattern, effect)

    @app.callback(
        *(Output(c2_t, "disabled") for c2_t in slicer_c2_slider_ids),
        Input("slicer_c2_enable", "value"),
        Input("slicer_c2_step_num", "value"),
        Input("slicer_c2_pattern", "value"),
        Input("slicer_c2_effect", "value"),
    )
    def _dis_c2_channels(enable, step_num, pattern, effect):
        return disable_channels(enable, step_num, pattern, effect)
