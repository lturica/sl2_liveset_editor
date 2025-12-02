
import dash_bootstrap_components as dbc


from sl2_dash.components.modals import ALL_MODALS
from sl2_dash.components.toasts import ALL_TOASTS

from sl2_dash.components.cards.global_parameters import global_cards
from sl2_dash.components.cards.slicer import slicer_c1_card
from sl2_dash.components.cards.phaser import  phaser_c1_card, phaser_c2_card
from sl2_dash.components.cards.flanger import flanger_c1_card, flanger_c2_card
from sl2_dash.components.cards.tremolo import  tremolo_c1_card, tremolo_c2_card
from sl2_dash.components.cards.overtone import  overtone_c1_card, overtone_c2_card
from sl2_dash.components.cards.beat import beat_card
from sl2_dash.components.cards.compressor import compressor_card
from sl2_dash.components.cards.divider import divider_card
from sl2_dash.components.cards.para_eq import para_eq_card
from sl2_dash.components.cards.mixer import mixer_card

from sl2_dash.components.cards.noise_supressor import noise_suppressor_card

parameter_cards = dbc.Tabs(
    [
        dbc.Tab([slicer_c1_card,],                   label="Slicer", tab_id="slicer_c12_tab"), 
        dbc.Tab([phaser_c1_card,phaser_c2_card],     label="Phaser", tab_id="phaser_c12_tab"),
        dbc.Tab([flanger_c1_card,flanger_c2_card],   label="Flanger ", tab_id="flanger_c12_tab"),
        dbc.Tab([tremolo_c1_card,tremolo_c2_card],   label="Tremolo", tab_id="tremolo_c12_tab"),
        dbc.Tab([overtone_c1_card,overtone_c2_card], label="Overtone", tab_id="overtone_c12_tab"),
        dbc.Tab(beat_card,                           label="Beat",       tab_id="beat_tab"),
        dbc.Tab(compressor_card,                     label="Compressor", tab_id="compressor_tab"),
        dbc.Tab(divider_card,                        label="Divider",    tab_id="divider_tab"),
        dbc.Tab(mixer_card,                          label="Mixer",      tab_id="mixer_tab"),
        dbc.Tab(noise_suppressor_card,               label="Noise Suppressor", tab_id="ns_tab"),
        dbc.Tab(para_eq_card,                        label="Parametric EQ",    tab_id="peq_tab"),
    ],
    id="parameter_tabs",
    active_tab="slicer_c12_tab",    # default visible tab
    class_name="parameter-tabs",
)



# Layout for the body of the page
body = dbc.Container(children=
                     ALL_MODALS +
                     ALL_TOASTS +
                     [dbc.Row([
        dbc.Col( global_cards, width=2),
        dbc.Col([parameter_cards,], width=10)
    ])],
    style={"padding-top": "10px"},
    fluid=True)