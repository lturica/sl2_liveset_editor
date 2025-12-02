import dash_bootstrap_components as dbc
from .common import make_tooltip, opts_from_enum, SLIDER_ARGS
from dash import html, dcc, Output, State


compressor_params = {"Enable": "compressor_enable"}
compressor_params.update({f"Param {i}": f"compressor_param_{i}" for i in range(1, 7)})

compressor_tts = {k: v + "_tt" for k, v in compressor_params.items()}

compressor_card = dbc.Card(
    [
        dbc.CardHeader(f"Compressor Parameters"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Enable", make_tooltip(compressor_tts["Enable"])]
                                ),
                                dbc.Switch(
                                    id=compressor_params["Enable"],
                                    value=False,
                                    label=None,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Sustain", make_tooltip(compressor_tts["Param 1"])]
                                ),
                                dcc.Slider(
                                    id=compressor_params["Param 1"],
                                    min=0,
                                    max=100,
                                    value=50,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Attack", make_tooltip(compressor_tts["Param 2"])]
                                ),
                                dcc.Slider(
                                    id=compressor_params["Param 2"],
                                    min=0,
                                    max=100,
                                    value=50,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Level", make_tooltip(compressor_tts["Param 3"])]
                                ),
                                dcc.Slider(
                                    id=compressor_params["Param 3"],
                                    min=0,
                                    max=100,
                                    value=60,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Tone", make_tooltip(compressor_tts["Param 4"])]
                                ),
                                dcc.Slider(
                                    id=compressor_params["Param 4"],
                                    min=0,
                                    max=100,
                                    value=50,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Ratio", make_tooltip(compressor_tts["Param 5"])]
                                ),
                                dcc.Slider(
                                    id=compressor_params["Param 5"],
                                    min=0,
                                    max=30,
                                    value=12,
                                    **SLIDER_ARGS,
                                ),
                            ],
                            width="auto",
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    [
                                        "Direct Mix",
                                        make_tooltip(compressor_tts["Param 6"]),
                                    ]
                                ),
                                dcc.Slider(
                                    id=compressor_params["Param 6"],
                                    min=0,
                                    max=30,
                                    value=0,
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
    id=f"compressor_params",
)

compressor_tts = compressor_tts.values()

compressor_outputs = [
    Output(cm, "value", allow_duplicate=True) for cm in compressor_params.values()
]

compressor_state = [State(cm, "value") for cm in compressor_params.values()]
