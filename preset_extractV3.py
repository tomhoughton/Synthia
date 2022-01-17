"""
TODO
- get_preset_dataV2
- save_training_data
- clear_new_presets
- innit
"""

# Imports:
import gzip
import os
from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
import numpy as np
import xmltodict
import json
from xml.dom import minidom
from Config import Config

class PresetManager_V3:
    
    # Create the constructor:
    def __init(self):
        self.training_json_folder = os.path.join('TrainingData', 'TrainingPresets')
        self.new_presets_folder = os.path.join('NewPresets')
        self.new_presets_json_folder = os.path.join('NewPresetsJson')
        self.new_presets = os.path.join('NewPresets')
        self.xml_export_path = os.path.join('NewPresetsXML')
        self.json_export_path = os.path.join('New{resetsJson')
        self.configObject = Config()

    # Clear the new presets folder:
    def clear_new_presets(self, usedPresets):
        
        adv_to_remove = self.add_fextensions(usedPresets, '.adv')
        json_to_remove = self.add_fextensions(usedPresets, '.json')

        for i, adv in enumerate(adv_to_remove):
            # Get os paths:
            adv_path = os.path.join(self.new_presets_folder)
            json_path = os.path.join(self.new_presets_json_folder, json_to_remove[i])

            # Remove file:
            os.remove(adv_path)
            os.remove(json_path)