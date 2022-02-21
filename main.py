import numpy as np
from preset_extract import Preset, PresetManager
from preset_extractV2 import PresetManager_V2, PresetV2
from preset_extractV3 import PresetManager_V3

manager = PresetManager_V3()

new_data = manager.get_new_data(folder='20thFeb')

print(new_data)

manager.save_training_data(presets=new_data)



