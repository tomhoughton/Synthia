import numpy as np
from preset_extract import Preset, PresetManager
from preset_extractV2 import PresetManager_V2, PresetV2
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

pm = PresetManager_V2()

a = pm.get_new_data_v3()

print(a[1])
