
# **SL-2 Live Set Editor**

A web-based editor for creating and modifying `.tsl` live sets for the **BOSS SL-2 Slicer** (which can be uploaded to the SL-2 using the **[Boss Tone Studio App](https://www.boss.info/us/support/by_product/sl-2/updates_drivers/)**).
This project is a continuation and expansion of the original *SL-2 Pattern Editor* by **Andrew Hill (u/BackgroundWasabi)**, rebuilt with a cleaner UI, full live set editing, clearer parameter descriptions.

The SL-2 is a very useful pedal: part slicer, part sequencer, part pseudo-synth, with some ability to be a flanger, phaser, octave and filter inside its patterns. Unfortunately, almost none of this is documented, and the official software only allows for a very small part of what the pedal seems capable of. This editor aims to make it easy to use the SL-2 to its full capacity.

An online hosted version of the tool is available **[here](https://4fad0fbc-8a65-4d85-878c-022dacd0e6dc.plotly.app/)**.
 

## **What this tool does today**

* Loads an entire SL-2 live set and allows you to edit every patch inside, and can also duplicate or delete the patches for more editing power
* Lets you inspect, edit, and rewrite all patterns in a patch
* Provides parameter descriptions (where known, otherwise there is a best-guess available)
* Allows you to load official BOSS preset live sets for editing or testing
* Lets you download modified `.tsl` files compatible with BOSS Tone Studio
* Includes notebooks with analyses of all official presets *(parameter distributions, histograms, pattern structure notes)*, which should be useful for any other developers 

None of this is meant to be "finished" at this stage.

 

## **Why this exists**

I took on this project because:

* the SL-2 is more powerful than it seems, as it has phaser, flanger, and octave effects included, besides the marketed tremolo
* the existing tools had great potential but were a little limited
* I wanted a place to share patches and see what others discover (which can be done in the future with updating the default .tsl offering)
* and because the SL-2 deserves a proper editor to unlock its full potential

With time, I hope this becomes a hub for:

* community-tested parameter knowledge
* interesting custom presets
* simple-to-edit effect-style slicer sets (fancy tremolos, or simply flanger, phaser, etc.)
* a full picture of how the signal paths work and what the parameters are for

**If you learn something new about the parameters, I would genuinely love to hear it. Raise an issue on this github to bring it up!**

 

## **Using the editor (web version)**

An online hosted version of the tool is available **[here](https://4fad0fbc-8a65-4d85-878c-022dacd0e6dc.plotly.app/)**.


You can upload a `.tsl` file, edit it, and download it again for use in BOSS Tone Studio. You can also find the pre-sets made by BOSS here

 

## **Running locally**

This project requires **Python 3.11**. Earlier versions may work but are not guaranteed.

### **1. Clone the repository**

```
git clone <your-repo-url>
cd <your-project-folder>
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

### **3. Run the app**

From the project root:

```
python3 app.py
```

Then open the printed localhost URL (usually `http://127.0.0.1:8050`, but printed in the console).

 

## **Included data & analysis**

The directory `info_and_ipynb/` contains:

* `tsl_file_contents.ipynb` — a structural breakdown of a `.tsl` live set
* `tsl_data_spread.ipynb` — histograms of every parameter across all official BOSS presets and raw preset data extracted from the factory live sets

These notebooks are meant to help anyone studying how the SL-2 works internally and they helped during the development of the webapp.

 

## **Credits**

* Original SL-2 Pattern Editor: **Andrew Hill (u/BackgroundWasabi)**
  [https://github.com/Andrew0Hill/SL2_Patch_Builder](https://github.com/Andrew0Hill/SL2_Patch_Builder)
* Parameter research: **u/CompetitionSuper7287**
* Documentation sources:

  * BOSS GT-1000 Parameter Guide
  * Roland SL-2 preset files
  * Various shared findings across the web 

This version was written and maintained by drann.
If you’d like to support the project: **[https://ko-fi.com/drann___](https://ko-fi.com/drann___)**

 

## **License**

MIT License.
This project is not affiliated with BOSS or Roland nor endorsed by them. All information contained within is publicly available.


  

# **Development TODO**

### **UI & Interaction Improvements**

* Add a way to move all slicer step sliders together (useful for quick envelope moving) and a restore to defaults button
* Improve the visual spacing and grouping of parameter sliders and switches
* Add a subtle highlight every 4th slicer step to make patterns easier to read at a glance in the "Slicer" section
* Explore a small, optional visualiser

  * e.g. draw the slicer pattern as an interactive plot
  * maybe even a quick audio preview tool (definitely out of scope for now, but would be fun)

* Investigate how BOSS Tone Studio actually uploads patches to the SL-2
  (RNA/MIDI? message ? something custom?) and make a way to upload to the SL-2 directly

### **Parameter & Behaviour Exploration**


* Document the behaviour of the most interesting / odd / simple patches in order to understand the parameters

  * especially ones that exhibit phaser-like or flanger-like or octave-like behaviour

* Continue refining parameter names, ranges, and descriptions as the community discovers more (have I mentioned I would appreciate help with that?)


### **Preset & Effect Development**

* Build a small library of simple effect-style slicer presets
* Provide a few starter presets inside the app to help new users understand the structure
* Begin thinking about a lightweight preset-sharing mechanism (local or online or just manually maintained by me)

### **Nice-to-Have Future Ideas**

* A patch comparison mode
* Some human-friendly parameter interpretations and a toggle to show "raw parameters" vs. "interpreted parameters"

