import dash
import re
from dash import Input, Output, State

from sl2_dash.components.cards.global_parameters import global_tts
from sl2_dash.components.cards.slicer import slicer_c1_tts, slicer_c2_tts
from sl2_dash.components.cards.phaser import phaser_c1_tts, phaser_c2_tts
from sl2_dash.components.cards.flanger import flanger_c1_tts, flanger_c2_tts
from sl2_dash.components.cards.tremolo import tremolo_c1_tts, tremolo_c2_tts
from sl2_dash.components.cards.overtone import overtone_c1_tts, overtone_c2_tts
from sl2_dash.components.cards.beat import beat_tts
from sl2_dash.components.cards.compressor import compressor_tts
from sl2_dash.components.cards.divider import divider_tts
from sl2_dash.components.cards.para_eq import para_eq_tts
from sl2_dash.components.cards.mixer import mixer_tts
from sl2_dash.components.cards.noise_supressor import noise_suppressor_tts


#################
# Help Tooltips #
#################


def modal_open(*args):
    # do not check because prevent_initial_call is True
    # if dash.callback_context.triggered_id is None:
    #    return dash.no_update
    return True


def register_tooltip_modals(app: dash.Dash) -> None:
    channel_tooltips = slicer_c1_tts + slicer_c2_tts
    channel_tooltips += phaser_c1_tts
    channel_tooltips += phaser_c2_tts
    channel_tooltips += flanger_c1_tts
    channel_tooltips += flanger_c2_tts
    channel_tooltips += tremolo_c1_tts
    channel_tooltips += tremolo_c2_tts
    channel_tooltips += overtone_c1_tts
    channel_tooltips += overtone_c2_tts

    # We have duplicate tooltip icons for each channel,
    # but we will open the same modal for both so we strip out the
    # c1 or c2 identifier when referencing the modal
    # channel identifier in the id (if it exists).
    cmatch = re.compile("_c\d+_")

    for name in channel_tooltips:
        if (
            "_enable_tt" in name
        ):  # through a miracle, the tooltips are 'slicer_enable_c1_tt' and 'phaser_c1_enable_tt', so this chooses the right ones

            @app.callback(
                Output(f"generic_enable_tt_modal", "is_open", allow_duplicate=True),
                Input(name, "n_clicks"),
                prevent_initial_call=True,
            )
            def _handle_enable_tooltips_noslicer(_):
                return modal_open()
        else:

            @app.callback(
                Output(
                    f"{cmatch.sub('_', name)}_modal", "is_open", allow_duplicate=True
                ),
                Input(name, "n_clicks"),
                prevent_initial_call=True,
            )
            def _handle_channel_tooltips(_):
                return modal_open()

    mono_fx_tooltips = []
    mono_fx_tooltips += global_tts
    mono_fx_tooltips += beat_tts
    mono_fx_tooltips += compressor_tts
    mono_fx_tooltips += divider_tts
    mono_fx_tooltips += mixer_tts
    mono_fx_tooltips += noise_suppressor_tts
    mono_fx_tooltips += para_eq_tts

    # this list of tooltip ids causes many errors to appear
    # they correspond to every parameter that appears  in the UI

    for name in mono_fx_tooltips:
        # tooltips for the enable button
        if "_enable" in name:

            @app.callback(
                Output(f"generic_enable_tt_modal", "is_open", allow_duplicate=True),
                Input(name, "n_clicks"),
                prevent_initial_call=True,
            )
            def _handle_enable_tooltips_noslicer(_):
                return modal_open()
        # tooltips for all other parameters
        else:

            @app.callback(
                Output(f"{name}_modal", "is_open"),
                Input(name, "n_clicks"),
                prevent_initial_call=True,
            )
            def _handle_mono_fx_tooltips(_):
                return modal_open()
