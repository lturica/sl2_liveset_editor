import dash_bootstrap_components as dbc
from dash import html, dcc, Output, State
from .common import make_tooltip, SLIDER_ARGS
from sl2_dash.components.ids import ChannelCopy

def create_overtone_channel_card(cnum: int):
    p_names = {"Enable": f"overtone_c{cnum}_enable"}
    p_names.update({f"Param {i}": f"overtone_c{cnum}_param_{i}" for i in range(1,9)})

    tt_names = {k: v + "_tt" for k, v in p_names.items()}

    if cnum ==2:
        copy_button = dbc.Button("Double-click to copy Channel 1 to Channel 2", 
                                 id=ChannelCopy.OVERTONE, 
                                 color="primary", 
                                 n_clicks=0,
                                 style={"marginTop": "25px",})
    else:
        copy_button = html.Div()


    card = dbc.Card([
        dbc.CardHeader( f"Overtone Channel {cnum} Parameters",),
        dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dbc.Label(["Enable", make_tooltip(tt_names["Enable"])]),
                dbc.Switch(value=False, id=p_names["Enable"], label=None)
            ], width="auto"),
            dbc.Col([
                dbc.Label(["Lower Level", make_tooltip(tt_names["Param 1"])]),
                dcc.Slider(id=p_names["Param 1"], min=0, max=100, value=50, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Upper Level", make_tooltip(tt_names["Param 2"])]),
                dcc.Slider(id=p_names["Param 2"], min=0, max=100, value=50, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Unison Level", make_tooltip(tt_names["Param 3"])]),
                dcc.Slider(id=p_names["Param 3"], min=0, max=100, value=50, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Direct Level", make_tooltip(tt_names["Param 4"])]),
                dcc.Slider(id=p_names["Param 4"], min=0, max=100, value=100, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Detune", make_tooltip(tt_names["Param 5"])]),
                dcc.Slider(id=p_names["Param 5"], min=0, max=100, value=35, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Low", make_tooltip(tt_names["Param 6"])]),
                dcc.Slider(id=p_names["Param 6"], min=0, max=100, value=50, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["High", make_tooltip(tt_names["Param 7"])]),
                dcc.Slider(id=p_names["Param 7"], min=0, max=100, value=50, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Output Mode", make_tooltip(tt_names["Param 8"])]),
                dcc.Slider(id=p_names["Param 8"], min=0, max=1, value=1, **SLIDER_ARGS)
            ],width="auto"),
            copy_button # button on channel 2 only
        ])
    ])],  id=f"overtone_c{cnum}_params")

    params = list(p_names.values())

    tooltips = list(tt_names.values())

    output = [Output(ov,"value",allow_duplicate=True) for ov in params]

    state = [State(ov,"value") for ov in params]

    return tooltips, card, output, state



overtone_c1_tts, overtone_c1_card, overtone_c1_outputs, overtone_c1_state = create_overtone_channel_card(1)
overtone_c2_tts, overtone_c2_card, overtone_c2_outputs, overtone_c2_state = create_overtone_channel_card(2)
