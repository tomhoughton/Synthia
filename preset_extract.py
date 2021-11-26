import gzip
import os
from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
import numpy as np
import xmltodict
import json
from xml.dom import minidom

""" 
We need to first unzip.
Then we need to try and figure out a way of looping through all the files.
Then we need to try and parse into json.
Then try send the data in an api.
"""

class PresetManager:
    def __init__(self, pr_categories, unzip_all=False) -> None:
        self.preset_path = os.path.join("Presets") # The path whre preset information is stored.
        self.analog_path = os.path.join(self.preset_path, "Analog") # Where the analog presets from ableton are stored.
        self.jsonn_path = os.path.join(self.preset_path, "JSON")
        self.categories = pr_categories # The categories from ableton analog.
        self.presets = []



    def getPresets(self):
        preset_list = [] # Create a list for the presets.

        # Loop through the categories:
        for category in self.categories:

            # Get the presets in the category folder:
            category_presets = os.listdir(os.path.join(self.analog_path, category))

            # Get the path for the category:
            category_path = os.path.join(self.analog_path, category)

            # Loop through the presets:
            for preset in category_presets:

                # Create a new preset object:
                new_preset = Preset(
                    preset,
                    category_path,
                    category
                )

                # Append preset to presed list:
                preset_list.append(new_preset)

        # Convert this to a numpy array:
        preset_np = np.array(preset_list)

        # Add this to the object.
        self.presets = preset_np
        return preset_np # Return the numpy array.


    def get_presets_via_json(self):

        preset_list = [] # Create a list for the presets"

        for category in self.categories:
            
            # Get the path for the category:
            category_path = os.path.join(self.jsonn_path, category)

            # Get the presets in the category folder:
            category_presets = os.listdir(category_path)

            for preset in category_presets:
                # Create a new preset object:
                new_preset = Preset(
                    preset,
                    category_path,
                    category
                )

                # Append preset to the list.
                preset_list.append(new_preset)
        
        # Convert this to a numpy array:
        preset_np = np.array(preset_list)

        self.presets = preset_np
        return preset_np
            


    def unzip(self, path, export_path):   
        export_with_category = os.path.join(export_path, "Bass")

        with gzip.open(path, 'r') as f:
            raw_xml = f.read()

            xml = ET.fromstring(raw_xml)
            tree = ET.ElementTree(xml)
            tree.write(os.path.join(export_with_category, "hello.xml"), encoding="utf-8")



    def unzip_category(self, presets, category_index):
        category_path = os.path.join(self.analog_path, self.categories[category_index])
        xml_path = os.path.join(self.preset_path, "XML")
        export_path = os.path.join(xml_path, "Bass")
        category_presets = os.listdir(category_path)

        for preset in category_presets:
            with gzip.open(os.path.join(category_path, preset), 'r') as file:
                
                preset_name = preset[:-3] + "xml"

                raw_xml = file.read()
                xml = ET.fromstring(raw_xml)
                tree = ET.ElementTree(xml)
                tree.write(os.path.join(export_path, preset_name), encoding="utf-8")

        print("Done")



    def covert_xml_category_to_json(self, category_index):
        # Create XML paths:
        xml_path = os.path.join(self.preset_path, "XML")
        xml_category_path = os.path.join(xml_path, self.categories[category_index])

        # Create JSON paths:
        json_path = os.path.join(self.preset_path, "JSON")
        json_category_path = os.path.join(json_path, self.categories[category_index])

        xml_category_presets = os.listdir(xml_category_path)

        for preset in xml_category_presets:

            xml_doc_path = os.path.join(xml_category_path, preset)
            xml_tree = ET.parse(xml_doc_path)

            root = xml_tree.getroot()

            to_string = ET.tostring(root, encoding='utf-8', method='xml')

            xml_to_dict = xmltodict.parse(to_string)

            json_name = preset[:-3] + "json"

            with open(os.path.join(json_category_path, json_name), "w") as json_file:
                json.dump(xml_to_dict, json_file, indent=2)


            
    def get_json_array(self, category_index):
        # Create JSON paths:
        json_path = os.path.join(self.preset_path, "JSON")
        json_category_path = os.path.join(json_path, self.categories[category_index])

        json_presets = os.listdir(json_category_path)

        rtn_data = []

        for preset in json_presets:
            with open(os.path.join(json_category_path, preset), "r") as json_file:
                data = json.load(json_file) 
            
            rtn_data.append(data)

        return rtn_data


        
class Preset:
    


    def __init__ (self, name, adv_path, category):
        self.name = name
        self.adv_path = adv_path
        self.category = category



    def get_name(self):
        return self.name



    def get_adv_path(self):
        return self.adv_path



    def get_category(self):
        return self.category


        