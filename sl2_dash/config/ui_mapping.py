from sl2_dash.components.cards.global_parameters import global_outputs, global_state

from sl2_dash.components.cards.slicer import (
    slicer_c1_outputs,
    slicer_c1_state,
    slicer_c2_outputs,
    slicer_c2_state,
)

from sl2_dash.components.cards.phaser import (
    phaser_c1_outputs,
    phaser_c1_state,
    phaser_c2_outputs,
    phaser_c2_state,
)

from sl2_dash.components.cards.flanger import (
    flanger_c1_outputs,
    flanger_c1_state,
    flanger_c2_outputs,
    flanger_c2_state,
)

from sl2_dash.components.cards.tremolo import (
    tremolo_c1_outputs,
    tremolo_c1_state,
    tremolo_c2_outputs,
    tremolo_c2_state,
)

from sl2_dash.components.cards.overtone import (
    overtone_c1_outputs,
    overtone_c1_state,
    overtone_c2_outputs,
    overtone_c2_state,
)

from sl2_dash.components.cards.beat import beat_outputs, beat_state

from sl2_dash.components.cards.compressor import compressor_outputs, compressor_state

from sl2_dash.components.cards.divider import divider_outputs, divider_state

from sl2_dash.components.cards.para_eq import para_eq_outputs, para_eq_state

from sl2_dash.components.cards.mixer import mixer_outputs, mixer_state

from sl2_dash.components.cards.noise_supressor import (
    noise_suppressor_outputs,
    noise_suppressor_state,
)


ALL_OUTPUTS = (
    global_outputs
    + slicer_c1_outputs
    + slicer_c2_outputs
    + phaser_c1_outputs
    + phaser_c2_outputs
    + flanger_c1_outputs
    + flanger_c2_outputs
    + tremolo_c1_outputs
    + tremolo_c2_outputs
    + overtone_c1_outputs
    + overtone_c2_outputs
    + beat_outputs
    + compressor_outputs
    + divider_outputs
    + mixer_outputs
    + noise_suppressor_outputs
    + para_eq_outputs
)
ALL_OUTPUTS_LEN = len(ALL_OUTPUTS)
ALL_STATES = (
    global_state,
    slicer_c1_state,
    slicer_c2_state,
    phaser_c1_state,
    phaser_c2_state,
    flanger_c1_state,
    flanger_c2_state,
    tremolo_c1_state,
    tremolo_c2_state,
    overtone_c1_state,
    overtone_c2_state,
    beat_state,
    compressor_state,
    divider_state,
    mixer_state,
    noise_suppressor_state,
    para_eq_state,
    # add states for other effects as you reintegrate them
)
# all_states gets flattened when used as inputs to functions
GROUP_LENGTHS = [len(state_list) for state_list in ALL_STATES]
