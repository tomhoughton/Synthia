import gzip
import os
import xml.etree.cElementTree as ET
import numpy as np

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
        self.categories = pr_categories # The categories from ableton analog.

        self.adv_paths = np.array([])

    def getPresetPaths(self):

        preset_list = []

        for category in self.categories:
            category_presets = os.listdir(os.path.join(self.analog_path, category))

            category_path = os.path.join(self.analog_path, category)

            for preset in category_presets:
                new_preset = Preset(
                    preset,
                    os.path.join(category_path, category),
                    category
                )
                preset_list.append(new_preset)

        # Convert this to a numpy array:
        preset_np = np.array(preset_list)

        return preset_np

    def unzip(self):
        example_preset = os.path.join(self.preset_path, "FatEric.adv")

        with gzip.open(example_preset, 'r') as f:
            raw_xml = f.read()

            xml = ET.fromstring(raw_xml)

            tree = ET.fromstring(raw_xml)
            tree.write("firstpreset.xml")

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
        