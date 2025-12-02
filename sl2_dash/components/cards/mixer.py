import dash_bootstrap_components as dbc
from .common import make_tooltip, opts_from_enum, SLIDER_ARGS
from dash import html, dcc, Output, State

mixer_params = {"Ch. 2 Bypass": "mixer_ch2_bypass",
                "Param 1": "mixer_param_1",
                "Param 2": "mixer_param_2",
                "Param 3": "mixer_param_3",
                "Param 4": "mixer_param_4"}
#mixer_params.update({f"Param {i}":f"mixer_param_{i}" for i in range(1,5)})

mixer_tts = {k:v+"_tt" for k,v in mixer_params.items()}

mixer_card = dbc.Card([
        dbc.CardHeader( f"Mixer Parameters"),
        dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dbc.Label(["Ch. 2 Bypass",make_tooltip(mixer_tts["Ch. 2 Bypass"])]),
                dbc.Switch(id=mixer_params["Ch. 2 Bypass"],value=0,label=None)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Direct Signal",make_tooltip(mixer_tts["Param 1"])]),
                dbc.Switch(id=mixer_params["Param 1"],value=1)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Direct Volume", make_tooltip(mixer_tts["Param 2"])]),
                dcc.Slider(id=mixer_params["Param 2"], min=0, max=127, value=100,**SLIDER_ARGS)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Sliced Signal", make_tooltip(mixer_tts["Param 3"])]),
                dbc.Switch(id=mixer_params["Param 3"],value=0)
            ],width="auto"),
            dbc.Col([
                dbc.Label(["Sliced Volume", make_tooltip(mixer_tts["Param 4"])]),
                dcc.Slider(id=mixer_params["Param 4"], min=0, max=100, value=100,**SLIDER_ARGS)
            ],width="auto")
        ])
    ])],
    
    id=f"mixer_params"
)

mixer_tts = mixer_tts.values()

mixer_outputs = [Output(mx, "value",allow_duplicate=True) for mx in mixer_params.values()]

mixer_state = [State(mx, "value") for mx in mixer_params.values()]