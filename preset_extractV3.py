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
    def __init__(self):
        self.training_json_folder = os.path.join('TrainingData', 'TrainingPresets')
        self.new_presets_folder = os.path.join('NewPresets')
        #self.new_presets_json_folder = os.path.join('NewPresetsJson')
        self.new_presets = os.path.join('NewPresets')
        self.xml_export_path = os.path.join('NewPresetsXML')
        self.json_export_path = os.path.join('NewPresetsJson')
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
            
    def get_new_data(self):
        """
        What should this function do:
        
        # Should check the allocated folder containing the presets.
        # Should then convert them into json.
        # Should then retreive all preset values then we'll go from there.
        # Should also apply the descriptor values to it in the json.
        
        """
        
        # Create an array of the new presets:
        presets_adv = os.listdir(self.new_presets_folder)
        
        # Loop through the presets:
        for index, preset in enumerate(presets_adv):
            # Export and save the xml files:
            adv_file = os.path.join(self.new_presets_folder, preset)
            xml_file_name = preset[:-3] + 'xml'
            
            # We then convert the adv file into an xml file:
            # Call to_xml function.
            self.to_xml(path=adv_file, export_path=self.xml_export_path, file_name=xml_file_name)
            
            # Then we get the xml file and convert it into a json file:
            json_file_name = preset[:-3] + 'json'
            xml_file = os.path.join(self.xml_export_path, xml_file_name)
            self.to_json(path=xml_file, export_path=self.json_export_path, file_name=json_file_name)
            
        # Gather all of the json files:
        json_files = os.listdir(os.path.join('NewPresetsJson'))
        
        
            
        
            
            
    def to_xml(self, path, export_path, file_name):
        with gzip.open(path, 'r') as f:
            raw_xml = f.read()
            
            xml = ET.fromstring(raw_xml)
            tree = ET.ElementTree(xml)
            tree.write(os.path.join(export_path, file_name), encoding='utf-8')
            
    def to_json(self, path, export_path, file_name):
        xml_tree = ET.parse(path)
        
        root = xml_tree.getroot()
        to_string = ET.tostring(root, encoding='utf-8', method='xml')
        xml_to_dict = xmltodict.parse(to_string)
        
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(xml_to_dict, json_file, indent=2)
        