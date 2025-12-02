import dash_bootstrap_components as dbc
from dash import html, dcc, Output, State
from .common import make_tooltip, SLIDER_ARGS
from sl2_dash.components.ids import ChannelCopy

def create_phaser_channel_card(cnum: int):
    p_names = {"Enable": f"phaser_c{cnum}_enable"}
    p_names.update({f"Param {i}": f"phaser_c{cnum}_param_{i}" for i in range(1,10)})

    tt_names = {k: v + "_tt" for k, v in p_names.items()}

    if cnum ==2:
        copy_button = dbc.Button("Double-click to copy Channel 1 to Channel 2", 
                                 id=ChannelCopy.PHASER, 
                                 color="primary",
                                 n_clicks=0,
                                 style={"marginTop": "25px",})
    else:
        copy_button = html.Div()


    card = dbc.Card([
        dbc.CardHeader( f"Phaser Channel {cnum} Parameters"),
        dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dbc.Label(["Enable", make_tooltip(tt_names["Enable"])]),
                dbc.Switch(value=False, id=p_names["Enable"], label=None)
            ], width="auto"),
            dbc.Col([
                dbc.Label(["Param 1", make_tooltip(tt_names["Param 1"])]),
                dcc.Slider(id=p_names["Param 1"], min=0, max=3, value=0, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 2", make_tooltip(tt_names["Param 2"])]),
                dcc.Slider(id=p_names["Param 2"], min=0, max=125, value=70, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 3", make_tooltip(tt_names["Param 3"])]),
                dcc.Slider(id=p_names["Param 3"], min=0, max=100, value=50, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 4", make_tooltip(tt_names["Param 4"])]),
                dcc.Slider(id=p_names["Param 4"], min=0, max=100, value=0, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 5", make_tooltip(tt_names["Param 5"])]),
                dcc.Slider(id=p_names["Param 5"], min=0, max=100, value=55, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 6", make_tooltip(tt_names["Param 6"])]),
                dcc.Slider(id=p_names["Param 6"], min=0, max=125, value=0, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 7", make_tooltip(tt_names["Param 7"])]),
                dcc.Slider(id=p_names["Param 7"], min=0, max=10, value=0, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 8", make_tooltip(tt_names["Param 8"])]),
                dcc.Slider(id=p_names["Param 8"], min=0, max=100, value=100, **SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Param 9", make_tooltip(tt_names["Param 9"])]),
                dcc.Slider(id=p_names["Param 9"], min=0, max=100, value=0, **SLIDER_ARGS)
            ],width="auto"),
            copy_button # button on channel 2 only
        ])
    ])],  id=f"phaser_c{cnum}_params")

    params = list(p_names.values())
    tooltips = list(tt_names.values())

    output = [Output(ph, "value",allow_duplicate=True) for ph in params]

    state = [State(ph,"value") for ph in params]

    return tooltips, card, output, state


# create cards and affiliated componenets
phaser_c1_tts, phaser_c1_card, phaser_c1_outputs, phaser_c1_state = create_phaser_channel_card(1)
phaser_c2_tts, phaser_c2_card, phaser_c2_outputs, phaser_c2_state = create_phaser_channel_card(2)
