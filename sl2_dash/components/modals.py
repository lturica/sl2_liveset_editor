import dash_bootstrap_components as dbc
from dash import html
from .ids import  Nav, GlobalSettings


ALL_MODALS = []

def register_modal(obj):
    """Decorator that registers a Modal in the ALL_MODALS list."""
    ALL_MODALS.append(obj)
    return obj


############################
# Navbar Modals and Delete #
############################

# Choose default patch from store modal
choose_default_tsl_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Choose default .tsl")),
        dbc.ModalBody([
                dbc.Label("Available .tsl files"),
                dbc.Select(
                    id=Nav.DEFAULT_DROPDOWN,
                    options=[],   # populated at open time
                    value=None,
                    style={"width": "100%"},
                ),
                html.Div( style={"marginTop": "0.5rem", "fontSize": "0.9rem"}),
            ]
        ),
        dbc.ModalFooter([
                dbc.Button("Load", id=Nav.LOAD_DEFAULT_BUTTON, color="primary", n_clicks=0),
            ]
        ),
    ],
    id="choose-default-modal",
    is_open=False,
    centered=True,
    )
)

# delete patch interactive modal
delete_patch_modal= register_modal(
    dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Delete current patch")),
            dbc.ModalBody([
                    dbc.Label("Are you sure you want to delete the current patch?"),
                    html.Div( style={"marginTop": "0.5rem", "fontSize": "0.9rem"}),
                ]
            ),
            dbc.ModalFooter([
                    dbc.Button("Delete", id=GlobalSettings.CONFIRM_DELETE_BUTTON, color="danger", n_clicks=0),
                ]
            ),
        ],
        id=GlobalSettings.CONFIRM_DELETE_MODAL,
        is_open=False,
        centered=True,
    )
)

# Disclaimer modal shows up when the site is opened for the first time, to explain the tool and current limitations.
instructions_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Instructions")),
        dbc.ModalBody([
            html.P("This tool is used to create and edit the .tsl patch files used through BOSS Tone Studio for the "
                " SL-2 Slicer effect pedal."),
            html.P('The navigation bar at the top allows you to upload your own live set, select a pre-built one, or download the current live set.'),
            html.P("The left column allows you to rename the live set and current patch. You can also change the current patch, duplicate it, or delete it. " \
                "When you duplicate or change the current patch, your changes (including the name) are immediately updated. " \
                "You must still download the live set in order to modify your local file."),
            html.P("The patch parameters can be edited in the main tabs in the centre of the UI. You can click on the help tooltips next to each parameter to view the information we currently "
                "have about it (if any)."),
            html.P("More information about the app, correctness of the labels, developers, license, and " \
                "more can be found in the About section in the navigation bar."),
            html.P("You can always open these instructions by clicking the instructions button at the top of this page."),
        ]),
    ], is_open=True, id = 'instructions_modal')
)

# Disclaimer modal shows up when the site is opened for the first time, to explain the tool and current limitations.
disclaimer_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("About This Tool")),
        dbc.ModalBody([
            html.P("The SL-2 Live Set Editor tool is currently under development. Many parameters (most of the non-slicer-effect-parameters) " \
                "have untested or generic names and descriptions assigned to them."),
                html.P("As we learn more about the functions of the unlabeled parameters, we will update the names, tooltip"
                " descriptions, and permissible value ranges."),
            html.P("If you encounter issues with the tool, have information about one of the parameters,"
                " or just have a suggestion, please open an issue on GitHub using the link in the header."),
            html.P("Thanks for trying out the tool, and happy slicing!"),
            html.Hr(),
            html.B('Credits'),
            html.P(["A lot of the information about the parameters originates from the " \
                "Parameter Guide for the BOSS GT-1000 Guitar Effects Processor, available ",
                html.A("here", href='https://www.boss.info/us/support/by_product/gt-1000/owners_manuals/', target="_blank"),' and ',
                html.A("here", href='https://www.zikinf.com/manuels/boss-gt-1000-parameter-guide-en-70162.pdf', target="_blank"),'. ',
                'This was originally identified by Redditor u/CompetitionSuper7287, and a comprehensive '
                'description of the information relevant to SL-2 can be found in this ',
                html.A("GitHub repo", href='https://github.com/pylonsarenice/SL2-Pattern-Editor', target="_blank"),
                ' or in this ',
                html.A("Google Doc", href='https://docs.google.com/document/d/1iCooADNApTqPilJJXJ9s6jXgYUmfDu4exT8Dbz0rzi8/edit?tab=t.0', target="_blank"),
                '.']),
            html.P(['Immense thanks to Andrew Hill (u/BackgroundWasabi), who built the original version of this app. '
                 'The original version can be found at ',
                    html.A("https://sl2-patch-editor.xyz/", href='https://sl2-patch-editor.xyz/', target="_blank"),
                    ' and in this ',
                    html.A("GitHub repo", href='https://github.com/Andrew0Hill/SL2_Patch_Builder', target="_blank"),
                    '.']),
            html.P([' The most recent update was lovingly made by u/_Drann. ' \
            'I am looking forward to feedback, ideas, and contributions. ' \
            'In particular, if you take the time to experiment with the parameters, let me know what you find. ' \
            'I have put together a rough Jupyter notebook with histograms of all the parameters in the pre-made .tsl files, '
            'and it can be found in the ',
                html.A('GitHub repo of this project',href='https://github.com/lturica/sl2_liveset_editor'),
                '.  ' ]),
            html.P(['If you would like to support me, find me ',
                html.A('here',href='https://ko-fi.com/drann___'),
                '.']),
            #html.P(' Please get in touch if these credits are incorrect.')
        ]),
        dbc.ModalFooter(
                html.P(["This tool is licensed under the MIT license, and provided as-is without any warranty. This tool"
                    " and its creators are not affiliated or endorsed in any way by BOSS or Roland Corporation. " \
                    "The pre-made SL-2 live sets available in this app are publicly distributed by Roland Corporation and available ",
                    html.A("here", href='https://bosstonecentral.com/liveset/category/sl-2/', target="_blank"),
                    ".",],
                    style={"font-size":"x-small","align":"left"})
        )
    ], is_open=False, id = 'info_modal')
)


###############################
# General Parameters Tooltips #
###############################

# Live set tooltip modal explains the live set name
live_set_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Live Set Name")),
        dbc.ModalBody([
            html.P("Sets the 'name' property of the .tsl file."),
            html.B("Note:"),
            html.P(" Currently, importing a .tsl file into Tone Studio sets 'name' property to the filename of the .tsl "
                " file you are importing, so this field will be overwritten when importing into Tone Studio if the filename is different.")
            ]
        )
    ], id="ls_name_tt_modal")
)

# Patch name modal
patch_name_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Patch Name")),
        dbc.ModalBody([
            html.P("Sets the name for the patch, as displayed in Tone Studio. " \
            "This name is updated in the 'Select Patch' list only when duplicating this patch or loading another patch. " \
            "All parameters are automatically saved when a patch is duplicated or a different patch is selected."),
            html.B("Note:"),
            html.P(" The PATCH%COM array (and, therefore, the Patch Name value) is limited to 16 characters.")
        ])
    ], id="patch_name_tt_modal")
)

# Patch name modal
select_patch_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Select Patch")),
        dbc.ModalBody([
            html.P("Choose a different patch to visualise. Click Edit Patch to display."),
            html.B("Notes:"),
            html.P("The name of the current patch is only updated when the a different patch is loaded." \
            "When a patch is duplicated, it is added at the end of this list. The duplicate will be the active patch." \
            "The order of this list cannot be changed at this time, but can be easily modified in Tone Studio.")
        ])
    ], id="select_patch_tt_modal")
)

# Format rev modal
format_rev_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Format Rev")),
        dbc.ModalBody([
            html.P("Sets the 'formatRev' of the .tsl file (?). "),
            html.B("Note:"),
            html.P("For now this value is only allowed to be '0001' until the scope of this value is confirmed.")
        ])
    ], id="format_rev_tt_modal")
)

# Memo modal
memo_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Memo")),
        dbc.ModalBody([
            html.P("Sets the 'memo' field in the .tsl file for the current patch."),
            html.B("Note:"),
            html.P("This is locked until the limitations of the Memo field are found through testing.")
        ])
    ], id="memo_tt_modal")
)

# Device modal
device_rev_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Device")),
        dbc.ModalBody([
            html.P("Sets the 'device' field in the .tsl file."),
            html.B("Note:"),
            html.P("This is locked to 'SL-2' for now.")
        ])
    ], id="device_tt_modal")
)

# Pattern modal
pattern_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Pattern Select")),
        dbc.ModalBody([
            html.P("Sets the pattern preset for the patch."),
            html.P("This can be a number of preset values, or 'USER' to enable a custom slicer patch."),
            html.P("The preset sounds are related to the original SL-20 patches."),
            html.B("Note:"),
            html.P("Any value other than 'USER' will disable all sliders, since the preset pattern will override any"
                " pattern defined using the sliders.")
        ])
    ], id="slicer_pattern_tt_modal")
)


####################
# Generic Tooltips #
####################

# Enable modal
generic_enable_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Enable")),
        dbc.ModalBody([
            html.P("Enables or disables the effect."),
            #html.B("Note:"),
            #html.P("Disabling the channel will also disable the sliders for all parameter arrays in the channel.")
        ])
    ], id="generic_enable_tt_modal")
)


#######################
# Slicer Tab Tooltips #
#######################

# Enable modal
slicer_enable_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Enable")),
        dbc.ModalBody([
            html.P("Enables or disables signal processing for this channel."),
            html.B("Note:"),
            html.P("Disabling the channel will also disable the sliders for all parameter arrays in the channel.")
        ])
    ], id="slicer_enable_tt_modal")
)

# Effect Type Modal
effect_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Effect Type")),
        dbc.ModalBody([
            html.P("Sets the type of effect used at each step."),
            html.P("If the value is set to 'PITCH', per-step pitch control is available in the Pitch Shift parameter"
                " array."),
            html.P("(If the value is anything other than 'PITCH', the Pitch Shift sliders are disabled since they have no "
                " effect in other modes.)"),
            html.B("Note:"),
            html.P("The effect names may not be completely correct yet.")
        ])
    ], id="slicer_effect_tt_modal")
)

# Step Number Modal
step_number_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Time-Step Number")),
        dbc.ModalBody([
            html.P("Divides each measure into this number equal steps, where each step can be modified using the"
                " Parameter Array sliders. "),
            html.B("Note:"),
            html.P("Choosing a value < STEP_24 will disable some sliders to indicate that these values will be ignored.")
        ])
    ], id="slicer_step_num_tt_modal")
)

# Parameter Arrays Modal
param_array_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Time Parameter Arrays")),
        dbc.ModalBody([
            html.P("The number of available time time steps is set by the Step Number dropdown list."),
            html.H5(html.B("Step Length")),
            html.P("Sets the length for each step in the pattern."),
            html.P("Values are [0-100] and represent the length of time audio is heard for this step (i.e. value=50 means"
                " that sound will be heard for 50% of the length of this step."),
            html.P("A value of 0 mutes sound completely, and a value of 100 means audio plays uninterrupted for"
                " this step."),
            html.H5(html.B("Step Level")),
            html.P("Values are [0-100] and represent relative volume/level of this step."),
            html.H5(html.B("Band Pass")),
            html.P("Sets a preset band pass filter value on each step."),
            html.P("Values are [0-6]. A value of 0 disables the filter, and values 1-6 apply a band pass filter."),
            html.H5(html.B("Effect Level")),
            html.P("Sets the level of the effect sound specified by 'Effect Type' for this step."),
            html.P("Values are [0-100] and represent relative level at each step."),
            html.H5(html.B("Pitch Shift")),
            html.P("Sets the amount of pitch shifting applied to this step."),
            html.P("Values are [0,24] where 0 is one octave below, and 24 is one octave above. Default is 12 (no shift)."),
            html.B("Note:"),
            html.P("Choosing a value other than 'PITCH' for Effect Type will disable these sliders, since they have"
                " no effect for other Effect Type modes.")
        ])
    ], id="slicer_param_arr_tt_modal")
)


#######################
# Phaser Tab Tooltips #
#######################

for i in range(9):
    phaser_parameter_n_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle(f"Phaser Parameter {1+i}")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. There are too many parameters here to assign to sliders, but some are obviously not appropriate for the SL-2."),
            
            html.B("TYPE"),
            html.P("Selects the PHASER type."),
            html.P("PRIME: An original BOSS phaser providing modulation not obtainable from previous units."),
            html.P("SCRIPT: Models the MXR Phase 90 manufactured in the ’70s."),

            html.B("STAGE"),
            html.P("Selects the number of stages used in the phaser effect: 2, 4, 8, 16, or 24."),

            html.B("RATE"),
            html.P("Sets the rate of the phaser effect."),
            html.P("When set to BPM, parameters follow the MASTER BPM for each patch."),
            html.P("If the BPM-based time exceeds the allowed range, it syncs to 1/2 or 1/4 of that period."),

            html.B("DEPTH"),
            html.P("Determines the depth of the phaser effect."),

            html.B("RESONANCE"),
            html.P("Sets the amount of resonance (feedback). Higher values emphasize the effect and create more unusual sounds."),

            html.B("MANUAL"),
            html.P("Adjusts the center frequency of the phaser effect."),

            html.B("WAVEFORM"),
            html.P("Selects the waveform type: TRI or SINE."),

            html.B("STEP RATE"),
            html.P("Sets the cycle of the step function that changes rate and depth."),
            html.P("Higher values produce finer steps."),
            html.P("Set to OFF to disable the step function."),
            html.P("When set to BPM, the step rate follows MASTER BPM with the same timing rules as RATE."),

            html.B("BI-PHASE"),
            html.P("ON connects the two phase-shift circuits in series; OFF disables series routing."),

            html.B("SEPARATION"),
            html.P("Adjusts diffusion (0–180 degrees). Higher values increase diffusion."),

            html.B("LOW DAMP"),
            html.P("Adjusts feedback for the low-frequency region (-100 to 0)."),

            html.B("HIGH DAMP"),
            html.P("Adjusts feedback for the high-frequency region (-100 to 0)."),

            html.B("LOW CUT"),
            html.P("Sets the low-cut filter frequency (FLAT or 20 Hz–20 kHz). FLAT disables the filter."),

            html.B("HIGH CUT"),
            html.P("Sets the high-cut filter frequency (20 Hz–20 kHz or FLAT). FLAT disables the filter."),

            html.B("DIRECT MIX"),
            html.P("Adjusts the volume of the direct sound."),

            html.B("BPM"),
            html.P("Sets the BPM for the patch (40–250)."),
            html.P("BPM indicates the number of quarter-note beats per minute."),
            html.P("When external MIDI is connected, MASTER BPM may sync to the MIDI device, preventing manual setting unless SYNC CLOCK is set to INTERNAL."),
        ])
    ], id=f"phaser_param_{i+1}_tt_modal") #phaser_param_1_tt_modal
)



########################
# Flanger Tab Tooltips #
########################

for i in range(10):
    flanger_parameter_n_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle(f"Flanger Parameter {1+i}")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. There are too many parameters here to assign to sliders, but some are obviously not appropriate for the SL-2."),
            
            html.B("RATE"),
            html.P("Sets the rate of the flanging effect."),
            html.P("When set to BPM, the parameter values follow the MASTER BPM setting for each patch."),
            html.P("If the BPM-based time exceeds the range of the effect, it syncs to 1/2 or 1/4 cycle."),

            html.B("DEPTH"),
            html.P("Determines the depth of the flanging effect."),

            html.B("RESONANCE"),
            html.P("Sets the resonance (feedback). Higher values emphasize the effect and create more unusual sounds."),

            html.B("MANUAL"),
            html.P("Adjusts the center frequency at which the flanger is applied."),

            html.B("TURBO"),
            html.P("ON produces a more intense flanger effect."),

            html.B("WAVEFORM"),
            html.P("Selects the waveform type: TRI or SINE."),

            html.B("STEP RATE"),
            html.P("Sets the rate of the step function that varies the flanger in discrete steps."),
            html.P("Higher values create smaller step increments."),
            html.P("Set to OFF to disable the step function."),
            html.P("BPM mode is also available for step syncing."),

            html.B("SEPARATION"),
            html.P("Adjusts diffusion (0–180 degrees). Higher values create more diffusion."),

            html.B("EFFECT LEVEL"),
            html.P("Adjusts the output level of the flanger effect."),

            html.B("LOW DAMP"),
            html.P("Adjusts the amount of feedback for low frequencies (-100 to 0)."),

            html.B("HIGH DAMP"),
            html.P("Adjusts the amount of feedback for high frequencies (-100 to 0)."),

            html.B("LOW CUT"),
            html.P("Sets the low-cut filter frequency (FLAT or 20 Hz–20 kHz). FLAT disables the low-cut filter."),

            html.B("HIGH CUT"),
            html.P("Sets the high-cut filter frequency (20 Hz–20 kHz or FLAT). FLAT disables the high-cut filter."),

            html.B("DIRECT MIX"),
            html.P("Adjusts the volume of the direct sound."),

            html.B("BPM"),
            html.P("Sets the BPM for the patch (40–250)."),
            html.P("BPM indicates the number of quarter-note beats per minute."),
            html.P("When external MIDI is connected, MASTER BPM may sync to the MIDI device, preventing manual setting unless SYNC CLOCK is set to INTERNAL."),

        ])
    ], id=f"flanger_param_{i+1}_tt_modal") #flanger_param_1_tt_modal
)




########################
# Tremolo Tab Tooltips #
########################


for i in range(5):
    tremolo_parameter_n_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle(f"Tremolo Parameter {1+i}")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. There are too many parameters here, but it is likely that TRIGGER and BPM are non-existent in the SL-2."),
            html.B('RATE') ,
            html.P('Adjusts the frequency (speed) of the change.') ,
            html.P('When set to BPM, the value of each parameter will be set according to the value of the “MASTER BPM” specified for each patch. This makes it easier to achieve effect sound settings that match the tempo of the song.'),
            html.P('If, due to the tempo, the time is longer than the range of allowable settings, it is then synchronized to a period either 1/2 or 1/4 of that time.'),
            html.B('DEPTH') ,
            html.P('Adjusts the depth of the effect.'),
            html.B('WAVEFORM') ,
            html.P('Adjusts changes in volume level. A higher value will steepen wave’s shape.'),
            html.B('EFFECT LEVEL'),
            html.P('Adjusts the volume.'),
            html.B('TRIGGER '),
            html.P('Turns the tremolo on/off.'),
            html.B('RISE TIME '),
            html.P('Specifies the time from when trigger turns on until the specified tremolo effect is obtained.'),
            html.B('DIRECT MIX '),
            html.P('Adjusts the volume of the direct sound.'),
            html.B('BPM '),
            html.P('Adjusts the BPM value for each patch.'),
            html.P('BPM (beats per minute) indicates the number of quarter note beats that occurmeach minute'),
            html.P('When you have an external MIDI device connected, the MASTER BPM synchronizes to the external MIDI devices tempo, making it impossible to set the MASTER BPM. To enable setting of the MASTER BPM, set “SYNC CLOCK” (P.39) to “INTERNAL.”'),
            html.P("The presets that have Tremolo enabled are: 'TREMOLO 5-**', 'SFX 7-08', 'McR Chord Fun', 'McR Dark Knight', 'McR Organ', 'TREMOLO WAVE', 'RISE UP'"),

        ])
    ], id=f"tremolo_param_{i+1}_tt_modal") #tremolo_param_1_tt_modal
)

#########################
# Overtone Tab Tooltips #
#########################


overtone_ll_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Lower Level")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the volume of the harmonic one octave below."),
        ])
    ], id="overtone_param_1_tt_modal")
)

overtone_hl_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Upper Level")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the volume of the harmonic one octave above."),
        ])
    ], id="overtone_param_2_tt_modal")
)

overtone_ul_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Unison Level")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the volume of added sound whose pitch is slightly shifted relative to the direct sound."),
        ])
    ], id="overtone_param_3_tt_modal")
)

overtone_dl_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Direct Level")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the volume of the direct sound."),
        ])
    ], id="overtone_param_4_tt_modal")
)


overtone_detune_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Detune")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the amount of the detune effect that adds depth to the sound."),
        ])
    ], id="overtone_param_5_tt_modal")
)


overtone_low_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Low")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the tonal character of the low-frequency range."),
        ])
    ], id="overtone_param_6_tt_modal")
)

overtone_high_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone High")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Adjusts the tonal character of the high-frequency range."),
        ])
    ], id="overtone_param_7_tt_modal")
)

overtone_mode_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Overtone Mode")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified. Parameters might be mismatched."),
            html.P("Selects the type of output between MONO and STEREO."),
        ])
    ], id="overtone_param_8_tt_modal")
)



#####################
# Beat Tab Tooltips #
#####################

# Beat Param 1
beat_p1_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Beat Param 1")),
        dbc.ModalBody([
            html.P("Param 1 is always 0 in the presets. The effect of changing this parameter is unknown."),
            #html.P("It is potentially related to")
        ])
    ], id="beat_param_1_tt_modal")
)

# Beat Param 2
beat_p2_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Beat Param 2")),
        dbc.ModalBody([
            html.P("Param 2 is always 1 in the presets (with one exception in TREMOLO_WAVE preset). The effect of changing this parameter is unknown."),
            #html.P("It is potentially related to ")
        ])
    ], id="beat_param_2_tt_modal")
)


###########################
# Compressor Tab Tooltips #
###########################

compressor_sustain_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Compressor Sustain")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the range (time) over which lowlevel signals are boosted. Larger values will result in longer sustain."),
        ])
    ], id="compressor_param_1_tt_modal")
)

compressor_attack_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Compressor Attack")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the strength of the attack when picking."),
        ])
    ], id="compressor_param_2_tt_modal")
)

compressor_level_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Compressor Level")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the volume."),
        ])
    ], id="compressor_param_3_tt_modal")
)

compressor_tone_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Compressor Tone")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the tone."),
        ])
    ], id="compressor_param_4_tt_modal")
)

compressor_ratio_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Compressor Ratio")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Selects the compression ratio."),
            html.P("In the presets, this takes values between 3 and 17."),
        ])
    ], id="compressor_param_5_tt_modal")
)

compressor_directmix_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Compressor Direct Mix")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the volume of the direct sound."),
            html.P("In the presets, this is 0 everywhere except for 'McR Ready 4 Beat', 'McR Techno 1', and 'McR Techno 2', where it is 30."),
        ])
    ], id="compressor_param_6_tt_modal")
)


########################
# Divider Tab Tooltips #
########################

# Divider Param 1
divider_p1_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Divider Param 1")),
        dbc.ModalBody([
            html.P("Param 1 ranges between 0 and 3 in the presets. The effect of changing this parameter is unknown."),
            html.P("It is potentially related to how the input signal is split and recombined.")
        ])
    ], id="divider_param_1_tt_modal")
)

# Divider Param 2
divider_p2_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Divider Param 2")),
        dbc.ModalBody([
            html.P("Param 2 is generally 9, but it ranges between 0 and 9 in the presets. The effect of changing this parameter is unknown."),
            html.P("It is potentially related to how the input signal is split and recombined.")
        ])
    ], id="divider_param_2_tt_modal")
)



######################
# Mixer Tab Tooltips #
######################

# Mixer Channel 2 Bypass Modal
mixer_bypass_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Mixer Channel 2 Bypass")),
        dbc.ModalBody([
            html.P("If enabled, this switch seems to bypass Slicer Channel 2. If you want to run two slicer patterns"
                " simultaneously, you will need to ensure that this switch is disabled."),
            html.P("It is unknown whether this switch also bypass the effects (Phaser, Tremolo, etc) for Channel 2"
                " as well.")
        ])
    ], id="mixer_ch2_bypass_tt_modal")
)

# Mixer P1
for i in range(4):
    mixer_param_n_modal = register_modal(
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle(f"Mixer Param {i+1}")),
            dbc.ModalBody([
                html.P('Experimenting shows that the Mixer settings affect the direct signal (to which the effects are applied)'
                ' and the sliced signal (that appears to only be affected by  the Slicer tab). The two sliders adjust the volumes' \
                ' of the direct and sliced signals. It is unknown if this is connected to the Divider parameters or if channels A and B can be crossed.'),
                html.P("Description from GT-1000 manual. To be verified. In the manual, the Divider and Mixer parameters are related to each other."),
                html.B('STEREO'),
                html.P('Channels “A” and “B” will be mixed and output in stereo.'),
                html.B('PAN' ),
                html.P('L/R Channels “A” and “B” will be assigned respectively to the L and R OUTPUT jacks.'),
                html.B('A/B BALANCE '),
                html.P('Adjusts the volume balance of channels “A” and “B.” This is shown only if DIVIDER MODE is set to “DUAL.”'),
                html.B('SPREAD' ),
                html.P('Slightly delays the sound of channel “B” to make the sound more spacious. This is shown only if DIVIDER MODE is set to “DUAL.”')
            ])
        ], id=f"mixer_param_{i+1}_tt_modal")#mixer_param_1_tt_modal
    )



#################################
# Noise Suppressor Tab Tooltips #
#################################

# Noise Suppressor Release
ns_release_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Noise Suppressor Release")),
        dbc.ModalBody([
            html.P("Description from GT-1000 manual. To be verified."),
            html.P("Adjusts the time from when the noise suppressor " \
            "begins to function until the noise level reaches 0."),
        ])
    ], id="noise_suppressor_release_tt_modal")
)

# Noise Suppressor Threshold
ns_threshold_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Noise Suppressor Threshold")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjust this parameter as appropriate for the volume of the noise. " \
            "If the noise level is high, a higher setting is appropriate. If the noise level is low, " \
            "a lower setting is appropriate. " \
            "Adjust this value until the decay of the guitar sound is as natural as possible. "),
            html.B('Note:'),
            html.P(" High settings for the threshold parameter may result "
            "in there being no sound when you play with your guitar volume turned down.")
        ])
    ], id="noise_suppressor_threshold_tt_modal")
)


##############################
# Parametric EQ Tab Tooltips #
##############################


peq_lg_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Low Gain")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the tone for the low frequency range."),
            html.P('0 represents -20dB; 20 represents +0dB; 40 represents +20dB.')
        ])
    ], id="para_eq_param_1_tt_modal")
)

peq_hg_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ High Gain")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the tone for the high frequency range."),
            html.P('0 represents -20dB; 20 represents +0dB; 40 represents +20dB.')
        ])
    ], id="para_eq_param_2_tt_modal")
)

peq_lvl_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Level")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the overall volume level of the equalizer."),
            html.P('0 represents -20dB; 20 represents +0dB; 40 represents +20dB.')

        ])
    ], id="para_eq_param_3_tt_modal")
)

peq_lmf_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Low-Mid Frequency")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Specifies the center of the frequency range that will be adjusted by the LOW-MID GAIN.")
        ])
    ], id="para_eq_param_4_tt_modal")
)

peq_lmq_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Low-Mid Q")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the width of the area affected by the EQ centered at the LOW-MID FREQ. Higher values will narrow the area.")
        ])
    ], id="para_eq_param_5_tt_modal")
)

peq_lmg_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Low-Mid Gain")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the low-middle frequency range tone."),
            html.P('0 represents -20dB; 20 represents +0dB; 40 represents +20dB.')
        ])
    ], id="para_eq_param_6_tt_modal")
)

peq_hmf_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ High-Mid Frequency")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Specifies the center of the frequency range that will be adjusted by the HIGH-MID GAIN.")
        ])
    ], id="para_eq_param_7_tt_modal")
)

peq_hmq_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ High-Mid Q")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the width of the area affected by the EQ centered at the HIGH-MID FREQ. Higher values will narrow the area.")
        ])
    ], id="para_eq_param_8_tt_modal")
)

peq_hmg_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ High-Mid Gain")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("Adjusts the high-middle frequency range tone."),
            html.P('0 represents -20dB; 20 represents +0dB; 40 represents +20dB.')

        ])
    ], id="para_eq_param_9_tt_modal")
)

peq_hc_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Low Cut")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("This sets the frequency at which the low cut filter begins to take effect."),
            html.B('Note:'),
            html.P("When set to 0, the low cut filter will have no effect.")
        ])
    ], id="para_eq_param_10_tt_modal")
)


peq_lc_modal = register_modal(
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Parametric EQ Low Cut")),
        dbc.ModalBody([
            html.P("Description from GT-1000 Manual. To be verified."),
            html.P("This sets the frequency at which the high cut filter begins to take effect. "),
            html.B('Note:'),
            html.P("When set to 30, the high cut filter will have no effect.")
        ])
    ], id="para_eq_param_11_tt_modal")
)