import numpy as np
from preset_extract import Preset, PresetManager
import os
import json

"""
Steps for next coding session:

* get rid of all instances of .DS_Store in the array
* start building out a simple API
* Convert all to JSON format
* Start looking at the data to see what is needed
* Could maybe create a little python program to help us out !!!!

STEPS FOR THE WEB APP:
* Get all the json data by unzipping all the xml files

JSON FILE STRUCTURE:
.Ableton .UltraAnalog .UserName

TASK FOR THIS BRANCH:

* Build a way to conveniently see all the preset names 
  and show a single value from that preset.

"""

# # Important variables:
# categories = np.array([
#     'Bass'
# ])

# # Create a preset manager instance.
# preset_manager = PresetManager(categories)

# data = preset_manager.get_preset_data()
# json = preset_manager.format_preset_data_for_api(data)

# preset_manager.check_for_new_presets()
