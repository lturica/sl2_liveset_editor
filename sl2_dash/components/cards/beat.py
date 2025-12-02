import dash_bootstrap_components as dbc
from .common import make_tooltip, opts_from_enum, SLIDER_ARGS
from dash import html, dcc, Output, State

beat_params = {"Param 1": "beat_param_1", "Param 2": "beat_param_2"}

beat_tts = {k: v + "_tt" for k, v in beat_params.items()}

beat_card = dbc.Card(
    [
        dbc.CardHeader(
            f"Beat Parameters",
        ),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Param 1", make_tooltip(beat_tts["Param 1"])]
                                ),
                                dcc.Slider(
                                    id=beat_params["Param 1"],
                                    min=0,
                                    max=1,
                                    value=0,
                                    disabled=False,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Param 2", make_tooltip(beat_tts["Param 2"])]
                                ),
                                dcc.Slider(
                                    id=beat_params["Param 2"],
                                    min=0,
                                    max=1,
                                    value=1,
                                    disabled=False,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                    ]
                )
            ]
        ),
    ],
    id=f"beat_params",
)

beat_tts = beat_tts.values()

beat_outputs = [Output(b, "value", allow_duplicate=True) for b in beat_params.values()]

beat_state = [State(beat, "value") for beat in beat_params.values()]
