import dash_bootstrap_components as dbc
from dash import html,dcc 
from sl2_dash.components.ids import Debug

debug_card = html.Div(
        dbc.Card(
            [
                dbc.CardHeader("Debug Info", id=Debug.DEBUG_CARD),
                dbc.CardBody(
                [
                    dbc.Label(' Choose Default in the navbar '),
                    html.Pre(id=Debug.DEBUG_TEXT_1, style={"whiteSpace": "pre-wrap"}),
                    html.Hr(),
                    dbc.Label(' debug2 '),
            
                    html.Pre(id=Debug.DEBUG_TEXT_2, style={"whiteSpace": "pre-wrap"}),
                    html.Hr(),
                    dbc.Label(' debug3'),
                    html.Pre(id=Debug.DEBUG_TEXT_3, style={"whiteSpace": "pre-wrap"}),
                    html.Hr(),
                    dbc.Label(' debug4 '),
                    html.Pre(id=Debug.DEBUG_TEXT_4, style={"whiteSpace": "pre-wrap"}),
                ]    
                )
            ]
        )
    )
