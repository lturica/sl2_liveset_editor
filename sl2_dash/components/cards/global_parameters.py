from sl2_dash.components.ids import GlobalSettings
from .common import make_tooltip

import dash_bootstrap_components as dbc
from dash import html, Output, State


liveset_name_card = dbc.Card(
    [
        dbc.CardHeader("Current File", id="name_card"),
        dbc.CardBody(
            [
                dbc.Col(
                    [
                        dbc.Label(["Live Set Name:", make_tooltip("ls_name_tt")]),
                        dbc.Input(
                            id=GlobalSettings.LIVE_SET_NAME,
                            value="New Live Set",
                            type="text",
                            valid=True,
                        ),
                    ],
                    width="auto",
                ),
                html.Div(
                    [
                        dbc.Col(
                            [
                                dbc.Label(
                                    ["Patch Name:", make_tooltip("patch_name_tt")]
                                ),
                                dbc.Input(
                                    id=GlobalSettings.PATCH_NAME,
                                    value="CUSTOM-PATCH-1",
                                    type="text",
                                    valid=True,
                                ),
                            ],
                            width="auto",
                        )
                    ],
                    style={
                        "marginTop": "10px",
                    },
                ),
                html.Div(
                    [
                        dbc.Row(
                            dbc.Button(
                                "Duplicate Patch",
                                id=GlobalSettings.PATCH_DUPLICATE_BUTTON,
                                color="primary",
                                className="mb-2",
                            )
                        ),
                        dbc.Row(
                            dbc.Button(
                                "Delete Patch",
                                id=GlobalSettings.PATCH_DELETE_BUTTON,
                                color="primary",
                            )
                        ),
                    ],
                    style={
                        "marginTop": "10px",
                        "marginLeft": "10px",
                        "marginRight": "10px",
                    },
                ),
            ]
        ),
    ]
)

global_pars_card = dbc.Card(
    [
        dbc.CardHeader("Other Parameters", id="glbl_params_card"),
        dbc.CardBody(
            dbc.Col(
                [
                    dbc.Col(
                        [
                            dbc.Label(["Memo:", make_tooltip("memo_tt")]),
                            dbc.Input(
                                id=GlobalSettings.MEMO,
                                value="",
                                type="text",
                                disabled=True,
                            ),
                        ],
                        width="auto",
                    ),
                    dbc.Col(
                        [
                            dbc.Label(["Format Rev:", make_tooltip("format_rev_tt")]),
                            dbc.Input(
                                id=GlobalSettings.LIVE_SET_FORMAT_REV,
                                value="0001",
                                type="text",
                                disabled=True,
                            ),
                        ],
                        width="auto",
                    ),
                    dbc.Col(
                        [
                            dbc.Label(["Device:", make_tooltip("device_tt")]),
                            dbc.Input(
                                id=GlobalSettings.LIVE_SET_DEVICE,
                                value="SL-2",
                                type="text",
                                disabled=True,
                            ),
                        ],
                        width="auto",
                    ),
                ]
            )
        ),
    ]
)

patch_selection_card = dbc.Card(
    [
        dbc.CardHeader("Select Patch", id="patch_selection_card"),
        dbc.CardBody(
            dbc.Col(
                [
                    dbc.Col(
                        [
                            dbc.Label(
                                ["Select Other Patch:", make_tooltip("select_patch_tt")]
                            ),
                            dbc.Select(
                                id=GlobalSettings.PATCH_SELECT_DROPDOWN,
                                options=[{"label": f"CUSTOM-PATCH-1", "value": 0}],
                                value="0",
                                style={"width": "100%"},
                            ),
                            # html.Div([
                            #    dbc.Row(dbc.Button("Edit Patch", id=GlobalSettings.PATCH_SELECT_BUTTON,  color="primary", className="mb-2", )),
                            #    ],
                            # style={"marginTop": "10px","marginLeft": "10px","marginRight": "10px"})
                        ],
                        width="auto",
                    ),
                ]
            )
        ),
    ]
)

global_tts = [
    "ls_name_tt",
    "patch_name_tt",
    "memo_tt",
    "format_rev_tt",
    "device_tt",
    "select_patch_tt",
]

global_cards = [liveset_name_card, patch_selection_card, global_pars_card]

global_outputs = [
    Output(lsp, "value", allow_duplicate=True) for lsp in GlobalSettings.global_list()
]

global_state = [State(lsp, "value") for lsp in GlobalSettings.global_list()]
