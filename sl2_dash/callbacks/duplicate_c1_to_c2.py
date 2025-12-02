from dash import Output, Input, State
import datetime
import dash
from sl2_dash.components.ids import ChannelCopy

from sl2_dash.components.cards.slicer import slicer_c1_state, slicer_c2_outputs
from sl2_dash.components.cards.phaser import phaser_c1_state, phaser_c2_outputs
from sl2_dash.components.cards.flanger import flanger_c1_state, flanger_c2_outputs
from sl2_dash.components.cards.tremolo import tremolo_c1_state, tremolo_c2_outputs
from sl2_dash.components.cards.overtone import overtone_c1_state, overtone_c2_outputs


copy_button_inputs = [Input(id, "n_clicks") for id in ChannelCopy.SLICER.values()] + [
    Input(ChannelCopy.PHASER, "n_clicks"),
    Input(ChannelCopy.FLANGER, "n_clicks"),
    Input(ChannelCopy.TREMOLO, "n_clicks"),
    Input(ChannelCopy.OVERTONE, "n_clicks"),
]


channel_1_states = [
    slicer_c1_state[(24 * i + 4) : (24 * (i + 1) + 4)] for i in range(5)
] + [phaser_c1_state, flanger_c1_state, tremolo_c1_state, overtone_c1_state]
channel_2_outputs = [
    slicer_c2_outputs[(24 * i + 4) : (24 * (i + 1) + 4)] for i in range(5)
] + [phaser_c2_outputs, flanger_c2_outputs, tremolo_c2_outputs, overtone_c2_outputs]


def register_copy_c1_c2_button_callbacks(app: dash.Dash) -> None:
    for i in range(len(copy_button_inputs)):

        @app.callback(
            Output(ChannelCopy.DOUBLE_CLICK_TIMESTAMP, "data", allow_duplicate=True),
            *channel_2_outputs[i],
            copy_button_inputs[i],
            State(ChannelCopy.DOUBLE_CLICK_TIMESTAMP, "data"),
            *channel_1_states[i],
            prevent_initial_call=True,
        )
        def _duplicate_c1_to_c2(n_clicks, timestamp, *args):
            # args are the states of the channel 1 data
            current_time = datetime.datetime.now()
            current_time_str = current_time.strftime(r"%d/%m/%y %H:%M:%S.%f")
            old_time = datetime.datetime.strptime(timestamp, r"%d/%m/%y %H:%M:%S.%f")

            # now_str = datetime.datetime.now().strftime(r'%d/%m/%y %H:%M:%S.%f')
            # now = datetime.datetime.strptime(now,r'%d/%m/%y %H:%M:%S.%f')
            if (
                current_time - old_time
            ).total_seconds() > 0.5:  # if less than 0.5 seconds, consider double click
                # single click registered
                return [current_time_str] + [dash.no_update] * len(args)
            else:
                # double-click registered and update values
                return [current_time_str] + list(args)
