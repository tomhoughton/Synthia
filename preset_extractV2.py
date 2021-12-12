"""
This file is what manages all of the data involved with this program.
It's roles include:
- Detecting new training data.
- Adding the new presets into the existing training data.
- CSV dataset creation (NOT IMPLETMENTED YET).
- Source and return all of the training data into json.
"""

"""
IMPORTS
"""
import gzip
import os
from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
import numpy as np
import xmltodict
import json
from xml.dom import minidom


class PresetManager_V2:
    def __init__(self):
        self.training_json_folder = os.path.join('TrainingData', 'TrainingPresets')
        self.NewPresets_folder = os.path.join('NewPresets')
        self.NewPresetsJson_folder = os.path.join('NewPresetsJson')
        self.new_presets = os.path.join('NewPresets')
        self.xml_export_path = os.path.join('NewPresetsXML')
        self.json_export_path = os.path.join('New{resetsJson')

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


    def write_json(self, export_path, file_name, data):
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(data, json_file)


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

    def refresh_stats(self):

        # This stores the low mid and high bands of the descriptors:
        descriptor_m = np.array([
            [0, 0, 0], # Consistency
            [0, 0, 0], # Brightness
            [0, 0, 0], # Dynamics
            [0, 0, 0] # Evolution
        ])

        total = 0 # Stores the total presets.

        presets = os.listdir(self.training_json_folder)

        for preset in presets:
            total += 1
            with open(os.path.join(self.training_json_folder, preset), 'r') as json_file:
                data = json.load(json_file)
                descriptors = [
                    data["descriptors"]["consistency"],
                    data["descriptors"]["brightness"],
                    data["descriptors"]["dynamics"],
                    data["descriptors"]["evolution"]
                ]

                for i, descrip in enumerate(descriptors):
                    if descrip > 66:
                        descriptor_m[i][2] = descriptor_m[i][2] + 1
                    elif descrip < 66 and descrip > 33:
                        descriptor_m[i][1] = descriptor_m[i][1] + 1
                    elif descrip < 33:
                        descriptor_m[i][0] = descriptor_m[i][0] + 1
        
        data = {
            'descriptorMatrix': descriptor_m,
            'totalPresets': total
        }

        return data





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