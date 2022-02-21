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
from DataFrameConfig import DataFrameConfig
import pandas as pd
from datetime import date

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
        self.data_f_config = DataFrameConfig()

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
       
            
    def get_new_data(self, folder):
        """
        What should this function do:
        
        # Should check the allocated folder containing the presets.
        # Should then convert them into json.
        # Should then retreive all preset values then we'll go from there.
        # Should also apply the descriptor values to it in the json.
        
        """
        
        # Create an array of the new presets:
        presets_adv_path = os.path.join(self.new_presets_folder, folder)
        presets_adv = os.listdir(presets_adv_path)
        
        # Loop through the presets:
        for index, preset in enumerate(presets_adv):
            # Export and save the xml files:
            adv_file = os.path.join(presets_adv_path, preset)
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
        
        new_data = []
        for preset in json_files:
            
            # Array to store new presets:
            
            # Store the preset name:
            name = ""
            
            # Create an empty dictionary to store preset values:
            values = {}
            
            with open(os.path.join(self.json_export_path, preset)) as json_file:
                data = json.load(json_file)
                
                # Obtain Preset Name:
                if len(data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]) > 0:
                    name = data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]
                else:
                    name = preset[:-5]
                    
            values['name'] = name
            
            # Get the global values;
            global_values = self.getGlobals(data)
            values['globals'] = global_values
            
            # Get Signal Chain 01:
            signal1 = self.getSignalChain1(data)
            values['SignalChain1'] = signal1
            
            # Get Signal Chain 02:
            signal2 = self.getSignalChain2(data)
            values['SignalChain2'] = signal2
            
            new_data.append(values)
        
        return new_data
            
                  
    def getGlobals(self, data):
        features = self.configObject.features
        values = {}
        for feature in features:
            pathTo = ["Ableton", "UltraAnalog"]
            try:
                #values.append({ feature: data[pathTo[0]][pathTo[1]][feature]["Manual"]["@Value"]})
                values[feature] = data[pathTo[0]][pathTo[1]][feature]["Manual"]["@Value"]
            except KeyError:
                #values.append({ feature: data[pathTo[0]][pathTo[1]][feature]["@Value"]})
                values[feature] = data[pathTo[0]][pathTo[1]][feature]["@Value"]

        return values
        
            
    def getSignalChain1(self, data):
        features = self.configObject.SCFeatures
        features.append(self.configObject.FilterToFilter2[0])
        values = {}
        for feature in features:
            pathTo = ["Ableton", "UltraAnalog", "SignalChain1"]
            try:
                #values.append({feature: data[pathTo[0]][pathTo[1]][pathTo[2]][feature]["Manual"]["@Value"]})
                values[feature] = data[pathTo[0]][pathTo[1]][pathTo[2]][feature]["Manual"]["@Value"]
            except KeyError:
                #values.append({ feature: data[pathTo[0]][pathTo[1]][pathTo[2]][feature]["@Value"]})
                values[feature] = data[pathTo[0]][pathTo[1]][pathTo[2]][feature]["@Value"]


        # ENV 1:
        # Need to get env features:
        envFeatures = self.configObject.ENVFeatures
        envValues = {}
        for i in envFeatures:
            #envValues.append({ i: data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"][i]["Manual"]["@Value"]})
            envValues[i] = data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"][i]["Manual"]["@Value"]
        
        # ENV 2:
        env2Values = {}
        for x in envFeatures: 
            #env2Values.append({ x: data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"][x]["Manual"]["@Value"]})
            env2Values[x] = data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"][x]["Manual"]["@Value"]

        # Add envelopes to the values dictionary.
        values["Envelope.0"] = envValues
        values["Envelope.1"] = env2Values

        rtn = values
        return rtn
    
    
    def getSignalChain2(self, data):
        features = self.configObject.SCFeatures2
        features.append(self.configObject.FilterToFilter2[1])
        values = {}
        for i in features:
                pathTo = ["Ableton", "UltraAnalog", "SignalChain2"]
                try:
                    #values.append({ i: data[pathTo[0]][pathTo[1]][pathTo[2]][i]["Manual"]["@Value"]})
                    values[i] = data[pathTo[0]][pathTo[1]][pathTo[2]][i]["Manual"]["@Value"]
                except KeyError:
                    #values.append({ i: data[pathTo[0]][pathTo[1]][pathTo[2]][i]["@Value"]})
                    values[i] = data[pathTo[0]][pathTo[1]][pathTo[2]][i]["@Value"]

        # ENV 1:
        # Need to get env features:
        envFeatures = self.configObject.ENVFeatures
        envValues = {}
        for i in envFeatures:
            #envValues.append({ i: data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"][i]["Manual"]["@Value"]})
            envValues[i] = data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"][i]["Manual"]["@Value"]
        
        # ENV 2:
        env2Values = {}
        for x in envFeatures: 
            #env2Values.append({ x: data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"][x]["Manual"]["@Value"]})
            env2Values[x] = data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"][x]["Manual"]["@Value"]

        # Add Envelopes to the values dictionary.
        values["Envelope.0"] = envValues
        values["Envelope.1"] = env2Values

        rtn = values
        return rtn
    
         
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
    
    
    def save_training_data(self, presets):
        """
        This saves the new presets as json files
        """
        
        # Need to get the path to export the json files:
        training_json_export = os.path.join('TrainingData', 'TrainingPresets')
        
        for preset in presets:
            preset_name = preset["name"] + '.json'
            self.write_json(training_json_export, preset_name, preset)
      
            
    def write_json(self, export_path, file_name, data):
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(data, json_file)
            

    def to_pandas(self):
        
        test_name = 'Default.json'
        training_json_path = os.path.join('TrainingData', 'TrainingPresets')
        data_frame_export_path = os.path.join('TrainingData', 'Datasets')
        today = date.today()
        date_str = today.strftime("%b-%d-%Y")
        
        dictionary = {}
        
        data_order = [self.data_f_config.signalChain, self.data_f_config.signalChain, self.data_f_config.globals]
        
        # Need to load the json file:
        with open(os.path.join(training_json_path, test_name)) as json_file:
            data = json.load(json_file)
            
            #Signal Chain 1:
            for parameter in self.data_f_config.signalChain:
                print(data['SignalChain1'][parameter])
                dictionary[parameter] = [data['SignalChain1'][parameter]]
            
            # Signal Chain 2:
            for parameter in self.data_f_config.signalChain:
                print(data['SignalChain2'][parameter])
                dictionary[parameter] = [data['SignalChain2'][parameter]]
                
            for parameter in self.data_f_config.globals:
                print(data['globals'][parameter])
                dictionary[parameter] = [data['globals'][parameter]]
                
            df = pd.DataFrame(data=dictionary)
            
            df.to_csv(os.path.join(data_frame_export_path, date_str))
            
            print(df)
            
            
        # def to_pandas_v2(self):
            
        #     # Get the path for the preset description json file:
        #     preset_description_path = os.path.join('PresetDescriptions')
            
            
                        