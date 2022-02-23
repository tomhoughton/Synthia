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
        self.new_preseet_path = os.path.join("NewPresets") # The path to the new presets.



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
            


    def get_preset_data(self):
        """
        This is to return a bunch of json to the dojo to see the different files.
        """

        presets = []

        # Get the json paths
        for category in self.categories:
            category_path = os.path.join(self.jsonn_path, category)
            category_presets = os.listdir(category_path)

            for preset in category_presets:

                values = []
                name = ""

                with open(os.path.join(category_path, preset)) as json_file:
                    data = json.load(json_file)
                    print("---------------------------------")
                    print(os.path.join(category_path, preset))
    
                    # Name
                    if len(data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]) > 0:
                        name = data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]
                    else:
                        name = preset[:-5]

                    """
                    Values for the parts that dont relate to the signal chain.
                    """
                    # One value
                    values.append(data["Ableton"]["UltraAnalog"]["Volume"]["Manual"]["@Value"]) # 0

                    """
                    Signal Chain 01
                    """
                    # Oscillator Toggle [1]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorToggle"]["Manual"]["@Value"])
                    
                    # Oscillator Waveshape [2]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorWaveShape"]["Manual"]["@Value"]) 

                    # Oscillator Oct [3]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorOct"]["Manual"]["@Value"]) 

                    # Oscillator Semitone [4]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorSemi"]["Manual"]["@Value"]) 

                    # Oscillator ENV Time [5]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorEnvTime"]["Manual"]["@Value"]) 

                    """
                    Signal Chain 02
                    """
                    # Oscillator Toggle [6]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorToggle"]["Manual"]["@Value"])
                    
                    # Oscillator Waveshape [7]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorWaveShape"]["Manual"]["@Value"]) 

                    # Oscillator Oct [8]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorOct"]["Manual"]["@Value"]) 

                    # Oscillator Semitone [9]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorSemi"]["Manual"]["@Value"]) 

                    # Oscillator ENV Time [10]:
                    values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorEnvTime"]["Manual"]["@Value"]) 

                    new_preset = PresetV2(name, values, 50, 50, 50, 50)
                    presets.append(new_preset)
        
        return presets

    def get_preset_dataV2(self):

        presets = []

        # Need to get the path to the training data:
        training_json_folder = os.path.join('TrainingData', 'TrainingPresets')

        training_presets = os.listdir(training_json_folder)

        for preset in training_presets:
            values = []

            with open(os.path.join(training_json_folder, preset)) as json_file:

                data = json.load(json_file)
                
                name = data["name"] 

                # Volume:
                values.append(data["volume"])

                # OscToggle01:
                values.append(data["OscToggle01"])

                # OscWaveShape01:
                values.append(data["OscWaveshape01"])

                # OscOctave01
                values.append(data["OscOctave01"])

                # OscSemi01:
                values.append(data["OscSemi01"])

                # OscEnvT01:
                values.append(data["OsvEnvT01"])

                # OscToggle 02:
                values.append(data["OscToggle02"])

                # Osc WaveShape 02:
                values.append(data["OscWaveshape02"])

                # Osc Octave02:
                values.append(data["OscOctave02"])

                # Osc Semi 02:
                values.append(data["OscSemi02"])

                # Osc Env02
                values.append(data["OscEnvT02"])

                """
                Descriptors:
                """
                brightness = data["descriptors"]["brightness"] 
                consistency = data["descriptors"]["consistency"] 
                dynamics = data["descriptors"]["dynamics"] 
                evolution = data["descriptors"]["evolution"] 

                new_preset = PresetV2(name, values, consistency, brightness, dynamics, evolution)
                presets.append(new_preset)

                
        return presets

    def check_for_new_presets(self): 
        """
        This functions role is to check the new presets folder,
        find the names for all the presets,
        then return a list of the preset namese to post
        """
        presets = os.listdir(self.new_preseet_path)
        new_preset_lst = ['hello'] # The list to store the new presets.



        return new_preset_lst

    def store_new_training_data(self, data):
        # Loop through the data:

        # Create a json file for each preset:
        return ''



    def format_preset_data_for_api(self, presets):
        preset_json_list = []
        for preset in presets:
            preset_json_list.append({ 'name': preset.name, 'volume': preset.volume})

        return preset_json_list

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
                tree.write(os.path.join(export_path, ), encoding="utf-8")

        print("Done")

    def get_new_data(self):
        # ADV Files:
        new_preset_path = os.path.join('NewPresets')
        presets = os.listdir(new_preset_path)
        export_path = os.path.join('NewPresetsAdv')

        #XML FILES:
        new_presets_xml = os.path.join('NewPresetsAdv')
        xml_presets = os.listdir(new_presets_xml)
        export_json_path = os.path.join('NewPresetsJson')

        if len(presets) >= 1:
            print('new')
            for preset in presets:
                # Convert the file into an adv file
                preset_path = os.path.join(new_preset_path, preset)
                name = preset[:-3] + 'xml'
                self.to_xml(preset_path, export_path, name)
            
            print('json')

            for xml_preset in xml_presets:
                xml_preset_path = os.path.join(new_presets_xml, xml_preset)
                name = xml_preset[:-3] + 'json'
                print(xml_preset)
                self.to_json(xml_preset_path, export_json_path, name)
                
        else:
            print('none')



    def get_new_data_v2(self):
        
        """
        This function checks the new presets folder to see if there are any new ones.
        Then return an array of PresetV2 objects for the program to use.

        Improvements:
        - Get it to delete the xml presets as they are not needed.
        - Get rid of the enumerate function as it is not needed.
        """

        # New presets path:
        new_presets = os.path.join('NewPresets')

        # New presets array:
        presets = os.listdir(new_presets)

        # XML export path:
        xml_export_path = os.path.join('NewPresetsXML')

        # Json export path:
        json_export_path = os.path.join('NewPresetsJson')


        # Store the new preset object:
        new_preset_obj = []

        # Loop through:
        for index, preset in enumerate(presets):

            # Export and save the xml files:
            adv_file = os.path.join(new_presets, preset)
            xml_file_name = preset[:-3] + 'xml'
            self.to_xml(adv_file, xml_export_path, xml_file_name)

            json_file_name = preset[:-3] + 'json'
            xml_file = os.path.join(xml_export_path, xml_file_name)
            self.to_json(xml_file, json_export_path, json_file_name)
            print('should be done')

        # Read through the completed json files:
        json_files = os.listdir(json_export_path)
        print('json folder length: ', len(json_files))

        for preset in json_files:
            print('iterate')
            values = []
            name = ""

            with open(os.path.join(json_export_path, preset)) as json_file:
                data = json.load(json_file)
                print('---------------------------')
                print(os.path.join(json_export_path, preset))

                # Name:
                if len(data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]) > 0:
                    name = data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]
                else:
                    name = preset[:-5]

            """
            Values not related to signal chains:
            """

            # One value [0]:
            values.append(data["Ableton"]["UltraAnalog"]["Volume"]["Manual"]["@Value"])

            """
            Signal Chain 01
            """
            # Oscillator Toggle [1]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorToggle"]["Manual"]["@Value"])

            # Oscillator Waveshape [2]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorWaveShape"]["Manual"]["@Value"])

            # Oscillator Octave [3]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorOct"]["Manual"]["@Value"])

            # Oscillator Semitone [4]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorSemi"]["Manual"]["@Value"])

            # Oscillator ENV Time [5]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorEnvTime"]["Manual"]["@Value"])

            """
            Signal Chain 02
            """

            # Oscillator Toggle [6]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorToggle"]["Manual"]["@Value"])

            # Oscillator Waveshape [7]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorWaveShape"]["Manual"]["@Value"])

            # Oscillator Osctave [8]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorOct"]["Manual"]["@Value"])

            # Oscillator Semitone [9]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorSemi"]["Manual"]["@Value"])

            # Psco;;atpr ENV Time [10]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorEnvTime"]["Manual"]["@Value"])

            # Append new preset and values to array.
            new_preset = PresetV2(name, values, 0, 0, 0, 0)
            new_preset_obj.append(new_preset)
        return new_preset_obj


    def to_xml(self, path, export_path, file_name):
        with gzip.open(path, 'r') as f:
            raw_xml = f.read()

            xml = ET.fromstring(raw_xml)
            tree = ET.ElementTree(xml)
            tree.write(os.path.join(export_path, file_name), encoding="utf-8")



    def to_json(self, path, export_path, file_name):
        xml_tree = ET.parse(path)

        root = xml_tree.getroot()
        to_string = ET.tostring(root, encoding='utf-8', method='xml')
        xml_to_dict = xmltodict.parse(to_string)
        
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(xml_to_dict, json_file, indent=2)


    def write_json(self, export_path, file_name, data):
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(data, json_file)

    def get_json_tree(self, presets):
        json_presets = []

        for preset in presets:
            json_presets.append(
                preset.format_to_json()
            )

        return { 'presets': json_presets }

    def save_training_data(self, presets):
        """
        This saves the new presets as json files.
        And then deletes the old 'new' presets.
        """

        # Need to get the path to export the json files:
        training_json_export = os.path.join('TrainingData', 'TrainingPresets')

        for preset in presets:
            preset_name = preset["name"] + '.json'
            self.write_json(training_json_export, preset_name, preset)


    def clear_NewPresets_folder(self, usedPresets):

        # Path to NewPresets:
        NewPresets_folder = os.path.join('NewPresets')
        NewPresetsJson_folder = os.path.join('NewPresetsJson')
        adv_to_remove = self.create_file_extensions(usedPresets, '.adv')
        json_to_remove = self.create_file_extensions(usedPresets, '.json')

        for index, adv in enumerate(adv_to_remove):
            # Generate the correct file paths:
            path_to_remove_adv = os.path.join(NewPresets_folder, adv)
            path_to_remove_json = os.path.join(NewPresetsJson_folder, json_to_remove[index])
            
            # Remove file:
            os.remove(path_to_remove_adv)
            os.remove(path_to_remove_json)

    def create_file_extensions(self, data, extension):
        temp = []
        for element in data:
            temp.append(element["name"] + extension)

        return temp
    

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

class PresetV2:
    def __init__ (self, name, values, consistency, brightness, dynamics, evolution):
        self.name = name
        self.volume = values[0]

        """
        Descriptors
        """
        self.consistency = consistency
        self.brightness = brightness
        self.dynamics = dynamics
        self.evolution = evolution

        """
        Signal Chain 01
        """
        self.OscToggle01 = values[1]
        self.OscWaveshape01 = values[2]
        self.OscOsctave01 = values[3]
        self.OscSemi01 = values[4]
        self.OscEnvT01 = values[5]

        """
        Signal Chain 02
        """
        self.OscToggle02 = values[6]
        self.OscWaveshape02 = values[7]
        self.OscOsctave02 = values[8]
        self.OscSemi02 = values[9]
        self.OscEnvT02 = values[10]

    def format_to_json(self):
        return {
            'name': self.name,
            'volume': self.volume,
            'OscToggle01': self.OscToggle01,
            'OscWaveshape01': self.OscWaveshape01,
            'OscOctave01': self.OscOsctave01,
            'OscSemi01': self.OscSemi01,
            'OsvEnvT01': self.OscEnvT01,
            'OscToggle02': self.OscToggle02,
            'OscWaveshape02': self.OscWaveshape02,
            'OscOctave02': self.OscOsctave02,
            'OscSemi02': self.OscSemi02,
            'OscEnvT02': self.OscEnvT02,
            'descriptors': {
                'consistency': self.consistency,
                'brightness': self.brightness,
                'dynamics': self.dynamics,
                'evolution': self.evolution
            }
        }
        
        
    """
    
        # Oscillator 02:
        pd_dictionary['OscillatorWaveShape02'] = []
        pd_dictionary['OscillatorOct02'] = []
        pd_dictionary['OscillatorSemi02'] = []
        pd_dictionary['OscillatorDetune02'] = []
        pd_dictionary['FilterCutoffFrequency02'] = []
        pd_dictionary['FilterLFOCutoffMod02'] = []
        pd_dictionary['FilterEnvCutoffMod02'] = []
        
        # Envelope 01:
        pd_dictionary['AttackTime01'] = []
        pd_dictionary['DecayTime01'] = []
        pd_dictionary['SustainLevel01'] = []
        pd_dictionary['SustainTime01'] = []
        pd_dictionary['ReleaseTime01'] = []
        
        # Envelope 02:
        pd_dictionary['AttackTime02'] = []
        pd_dictionary['DecayTime02'] = []
        pd_dictionary['SustainLevel02'] = []
        pd_dictionary['SustainTime02'] = []
        pd_dictionary['ReleaseTime02'] = []
        
    
    """