import dash_bootstrap_components as dbc
from sl2.params import slicer
from itertools import chain
from dash import dcc, Output, State, html
from .common import make_tooltip, opts_from_enum, SLIDER_ARGS
from sl2_dash.components.ids import ChannelCopy


# Types of slider for each channel
SLIDER_TYPES = [
    ("step_length", {"min": 0, "max": 100, "value": 50}),
    ("step_level", {"min": 0, "max": 100, "value": 100}),
    ("band_pass", {"min": 0, "max": 6, "value": 0}),
    ("effect_level", {"min": 0, "max": 100, "value": 50}),
    ("pitch_shift", {"min": 0, "max": 24, "value": 12}),
]

SLIDER_LABELS = [
    ("step_length", "Step Length"),
    ("step_level", "Step Level"),
    ("band_pass", "Band Pass"),
    ("effect_level", "Effect Level"),
    ("pitch_shift", "Pitch Shift"),
]


# Number of slider groups
N_SLIDER_GROUPS = len(SLIDER_TYPES)

# Number of sliders per group
N_CHANNELS = 24


def make_slider_group(id, cargs):
    return [
        dbc.Col(
            dcc.Slider(
                id=f"{id}_s{i}",
                disabled=(i >= 8) or id.startswith("pitch_shift"),
                **cargs,
                **SLIDER_ARGS,
            ),
            style={"width": "0px"},
        )
        for i in range(N_CHANNELS)
    ]


def create_slicer_2channels_card():
    # generate sliders list with args from slider types and slider args

    def sliders_and_names(cnum: int):
        sliders_dict = {
            s_t: make_slider_group(f"{s_t}_c{cnum}", cargs=args)
            for s_t, args in SLIDER_TYPES
        }
        s_names = {
            s_t: [v.children.id for v in v_t] for s_t, v_t in sliders_dict.items()
        }

        p_names = {
            "Pattern": f"slicer_c{cnum}_pattern",
            "Enable": f"slicer_c{cnum}_enable",
            "Effect": f"slicer_c{cnum}_effect",
            "Step Num": f"slicer_c{cnum}_step_num",
        }

        tt_names = {
            "Pattern": f"slicer_pattern_c{cnum}_tt",
            "Enable": f"slicer_enable_c{cnum}_tt",
            "Effect": f"slicer_effect_c{cnum}_tt",
            "Step Num": f"slicer_step_num_c{cnum}_tt",
        }
        return sliders_dict, s_names, p_names, tt_names

    sliders_dict_1, s_names_1, p_names_1, tt_names_1 = sliders_and_names(1)
    tt_names_1.update({"Parameter Arrays": f"slicer_param_arr_c1_tt"})

    sliders_dict_2, s_names_2, p_names_2, tt_names_2 = sliders_and_names(2)

    def make_channel_parameter_card(cnum, p_names, tt_names):
        top_params_card = dbc.Card(
            [
                dbc.CardHeader(
                    f"Slicer Channel {cnum} Parameters",
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label(
                                            ["Enable", make_tooltip(tt_names["Enable"])]
                                        ),
                                        dbc.Switch(
                                            value=True,
                                            id=p_names["Enable"],
                                            label=None,
                                        ),
                                    ],
                                    width="auto",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label(
                                            [
                                                "Pattern Select:",
                                                make_tooltip(tt_names["Pattern"]),
                                            ]
                                        ),
                                        dbc.Select(
                                            id=p_names["Pattern"],
                                            options=opts_from_enum(slicer.PATTERN),
                                            value=str(slicer.PATTERN.USER.value),
                                            disabled=False,
                                        ),
                                    ],
                                    width="auto",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label(
                                            [
                                                "Effect Type:",
                                                make_tooltip(tt_names["Effect"]),
                                            ]
                                        ),
                                        dbc.Select(
                                            id=p_names["Effect"],
                                            options=opts_from_enum(slicer.FX_TYPE),
                                            value=str(slicer.FX_TYPE.OFF.value),
                                            disabled=False,
                                        ),
                                    ],
                                    width="auto",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Label(
                                            [
                                                "Time-Step Number:",
                                                make_tooltip(tt_names["Step Num"]),
                                            ]
                                        ),
                                        dbc.Select(
                                            id=p_names["Step Num"],
                                            options=[
                                                {"label": "8 Steps", "value": 0},
                                                {"label": "12 Steps", "value": 1},
                                                {"label": "16 Steps", "value": 2},
                                                {"label": "24 Steps", "value": 3},
                                            ],
                                            value="0",
                                            # options=opts_from_enum(slicer.STEP_NUMBER),
                                            # value=str(slicer.STEP_NUMBER.STEP_8.value),
                                            disabled=False,
                                        ),
                                    ],
                                    width="auto",
                                ),
                            ],
                            style={"padding-bottom": "15px"},
                        ),
                    ]
                ),
            ],
            id=f"slicer-params-{cnum}",
        )
        return top_params_card

    slider_tab_card = dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        dbc.Label(
                            [
                                "Time-Step Parameter Arrays:",
                                make_tooltip(tt_names_1["Parameter Arrays"]),
                            ]
                        )
                    ),
                    dbc.Row(
                        [
                            dbc.Tabs(
                                [
                                    dbc.Tab(
                                        children=[
                                            dbc.Label(
                                                "Channel 1", style={"marginTop": "10px"}
                                            ),
                                            dbc.Row(sliders_dict_1[slider_type]),
                                            html.Hr(),
                                            dbc.Label(
                                                "Channel 2",
                                                style={"marginTop": "-20px"},
                                            ),
                                            dbc.Row(sliders_dict_2[slider_type]),
                                            html.Div(
                                                dbc.Row(
                                                    dbc.Button(
                                                        "Double-click to copy Channel 1 to Channel 2",
                                                        id=ChannelCopy.SLICER[
                                                            slider_type
                                                        ],
                                                        color="primary",
                                                        n_clicks=0,
                                                    )
                                                ),
                                                style={"marginTop": "30px"},
                                            ),
                                        ],
                                        label=slider_label,
                                        tab_id=f"slicer_{slider_type}",
                                    )
                                    for slider_type, slider_label in SLIDER_LABELS
                                ],
                                id=f"slicer_tabs",
                                active_tab=f"slicer_step_length",
                            )
                        ],
                    ),
                ],
                className="h-100",
            )
        ],
        id=f"slicer_sliders",
    )

    slicer_cards = dbc.Container(
        [
            # top row: two cards side by side
            dbc.Row(
                [
                    dbc.Col(  # channel card 1
                        make_channel_parameter_card(1, p_names_1, tt_names_1),
                        width=6,
                    ),
                    dbc.Col(  # channel card 2
                        make_channel_parameter_card(2, p_names_2, tt_names_2),
                        width=6,
                    ),
                ],
                class_name="g-0",  # remove space between the two cards
            ),
            # bottom row: one card spanning full width
            dbc.Row(
                dbc.Col(
                    slider_tab_card,
                    width=12,
                ),
                class_name="g-0 mt-0",  # no spacing above
            ),
        ],
        fluid=True,
        class_name="p-0",  # remove outer padding
    )

    params1 = list(p_names_1.values())
    tooltips1 = list(tt_names_1.values())
    sliders1 = list(chain.from_iterable(s_names_1.values()))
    outputs1 = [Output(sl, "value", allow_duplicate=True) for sl in params1 + sliders1]
    states1 = [State(sl, "value") for sl in params1 + sliders1]

    params2 = list(p_names_2.values())
    tooltips2 = list(tt_names_2.values())
    sliders2 = list(chain.from_iterable(s_names_2.values()))
    outputs2 = [Output(sl, "value", allow_duplicate=True) for sl in params2 + sliders2]
    states2 = [State(sl, "value") for sl in params2 + sliders2]

    return (
        slicer_cards,
        tooltips1,
        outputs1,
        states1,
        sliders1,
        tooltips2,
        outputs2,
        states2,
        sliders2,
    )


(
    slicer_c1_card,
    slicer_c1_tts,
    slicer_c1_outputs,
    slicer_c1_state,
    slicer_c1_slider_ids,
    slicer_c2_tts,
    slicer_c2_outputs,
    slicer_c2_state,
    slicer_c2_slider_ids,
) = create_slicer_2channels_card()
