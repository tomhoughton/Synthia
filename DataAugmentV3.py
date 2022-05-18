""" 
- Firstly we need to create the chunking algorithm:
- Then Add the augmentation rules
"""

# Imports:
import os
from turtle import st
import pandas as pd
import platform
from datetime import date
import numpy as np
from SynthiaStats import SynthiaStats
import random

class Augmentor:
    def __init__(self, df, date, audible_diff_range) -> None:
        # Augmented Dataset export path:
        self.export_path = os.path.join('TrainingData', 'AugmentedDatasets')

        # We need to get dataset:
        self.df = df

        # Store the binary permutations for the augmentation algorithm:
        self.combinations = []

        # Audible difference :
        # This variable is here to be the default range in which we can add or subract values to augment them.
        self.audible_difference_range = audible_diff_range 

        # So we need to also read and obtain the directories of where the statistics are located:
        self.date_var = date # Store the date of the of the statistics that we'll use. 
        self.path_to_stats = os.path.join('Statistics', self.date_var)
        self.consistency_path = os.path.join(self.path_to_stats, 'ConsistencyMinMaxMean')
        self.brightness_path = os.path.join(self.path_to_stats, 'BrightnessMinMaxMean')
        self.dynamics_path = os.path.join(self.path_to_stats, 'DynamicsMinMaxMean')
        self.evolution_path = os.path.join(self.path_to_stats, 'EvolutionMinMaxMean')

        # We need to store the stats for all of the descriptors:
        self.consistency_stats = None
        self.dynamics_stats = None
        self.brightness_stats = None
        self.evolution_stats = None

        # Holds the descriptive data:
        self.meta = [
            'Name',
            'Type',
            'Consistent',
            'Bright',
            'Evolves',
            'Dynamic',
            'Consistency',
            'Brightness',
            'Evolution',
            'Dynamics',
            'KeyboardUnisonToggle'
        ]

        # Values 2: this will essentially be a more refined structure of the current values variable.
        # Goes in the order of Feature, Preserve, Descriptor
        self.values_2 = [
            ['OscillatorWaveShape', 'Preserve', 'Consistency'],
            ['OscillatorOct', 'Preserve', 'Consistency'],
            ['OscillatorSemi', 'Preserve', 'Consistency'],
            ['OscillatorDetune', 'None', 'Consistency'],
            ['FilterCutoffFrequency', 'None', 'Brightness'],
            ['FilterLFOCutoffMod', 'None', 'Evolution'],
            ['FilterEnvCutoffMod', 'None', 'Evolution'],
            ['LFOSpeed', 'None', 'Evolution'],
            ['LFOFadeIn', 'Preserve', 'Evolution'],
            ['OscillatorWaveShape2', 'Preserve', 'Consistency'],
            ['OscillatorOct2', 'Preserve', 'Consistency'],
            ['OscillatorSemi2', 'Preserve', 'Consistency'],
            ['OscillatorDetune2', 'None', 'Consistency'],
            ['AttackTime', 'None', 'Dynamics'],
            ['DecayTime', 'None', 'Dynamics'],
            ['SustainLevel', 'None', 'Dynamics'],
            ['SustainTime', 'None', 'Dynamics'],
            ['ReleaseTime', 'None', 'Dynamics'],
            ['AttackTime2', 'None', 'Dynamics'],
            ['DecayTime2', 'None', 'Dynamics'],
            ['SustainLevel2', 'None', 'Dynamics'],
            ['SustainTime2', 'None', 'Dynamics'],
            ['ReleaseTime2', 'None', 'Dynamics'],
            ['VibratoSpeed', 'None', 'Consistency'],
            ['VibratoAmount', 'None', 'Consistency'],
            ['KeyboardUnison', 'Preserve', 'Consistency'],
            ['KeyboardDetune', 'None', 'Consistency']
        ]

        # We now need to figure out the combinations:
        self.combinations = [
            [0, 0, 0], 
            [0, 0, 1], 
            [0, 0, 2], 
            [0, 1, 0], 
            [0, 1, 1], 
            [0, 1, 2], 
            [0, 2, 0], 
            [0, 2, 1], 
            [0, 2, 2], 
            [1, 0, 0], 
            [1, 0, 1], 
            [1, 0, 2], 
            [1, 1, 0], 
            [1, 1, 1], 
            [1, 1, 2], 
            [1, 2, 0], 
            [1, 2, 1], 
            [1, 2, 2], 
            [2, 0, 0], 
            [2, 0, 1], 
            [2, 0, 2], 
            [2, 1, 0], 
            [2, 1, 1], 
            [2, 1, 2], 
            [2, 2, 0], 
            [2, 2, 1], 
            [2, 2, 2]
        ]

    def apply_meta_data(self, row, combination):
        rtn = [] # Store the return data.
        
        for m in self.meta:
            if m == 'Name':
                rtn.append(row[m] + "_" + str(combination))
            else:
                rtn.append(row[m])

        return rtn

    def augment_value(self, value, rule, operator):
        scalar = random.uniform(0, self.audible_difference_range)

        if (rule == "Preserve"): # Check for the preserve rule.
            return value

        if (operator == 0): # 0 = Minus
            
            if value == 0:
                return value


            new_value = value - scalar

            # Add some checks for the number:
            if new_value < 0:
                new_value = 0

            return new_value
        elif (operator == 1): # 1 = Nothing
            return value
        elif (operator == 2): # 2 = Add
            new_value = value + scalar
            return new_value

        return 69 # Just in case this doesn't work, I'll know.

    def add_to_data_frame(self, new_rows):
        pd_dictionary = {}
        # Descriptors 01:
        pd_dictionary['Name'] = []
        pd_dictionary['Type'] = []
        pd_dictionary['Consistent'] = []
        pd_dictionary['Bright'] = []
        pd_dictionary['Evolves'] = []
        pd_dictionary['Dynamic'] = []
        pd_dictionary['Consistency'] = []
        pd_dictionary['Brightness'] = []
        pd_dictionary['Evolution'] = []
        pd_dictionary['Dynamics'] = []

        # Oscillator 01:
        pd_dictionary['OscillatorWaveShape'] = []
        pd_dictionary['OscillatorOct'] = []
        pd_dictionary['OscillatorSemi'] = []
        pd_dictionary['OscillatorDetune'] = []

        # Filter and LFO:
        pd_dictionary['FilterCutoffFrequency'] = []
        pd_dictionary['FilterLFOCutoffMod'] = []
        pd_dictionary['FilterEnvCutoffMod'] = []
        pd_dictionary['LFOSpeed'] = []
        pd_dictionary['LFOFadeIn'] = []

        # Oscillator 02:
        pd_dictionary['OscillatorWaveShape2'] = []
        pd_dictionary['OscillatorOct2'] = []
        pd_dictionary['OscillatorSemi2'] = []
        pd_dictionary['OscillatorDetune2'] = []

        # Envelope 01:
        pd_dictionary['AttackTime'] = []
        pd_dictionary['DecayTime'] = []
        pd_dictionary['SustainLevel'] = []
        pd_dictionary['SustainTime'] = []
        pd_dictionary['ReleaseTime'] = []

        # Envelope 02:
        pd_dictionary['AttackTime2'] = []
        pd_dictionary['DecayTime2'] = []
        pd_dictionary['SustainLevel2'] = []
        pd_dictionary['SustainTime2'] = []
        pd_dictionary['ReleaseTime2'] = []

        # Globals:
        pd_dictionary['VibratoSpeed'] = []
        pd_dictionary['VibratoAmount'] = []
        pd_dictionary['KeyboardUnison'] = []
        pd_dictionary['KeyboardUnisonToggle'] = []
        pd_dictionary['KeyboardDetune'] = []

        for row in new_rows:
            # Meta:
            for index, m in enumerate(self.meta):
                pd_dictionary[m].append(row[index])


            # Values:
            row_slice = row[len(self.meta):]

            for index, v in enumerate(self.values_2):
                pd_dictionary[v[0]].append(row_slice[index])
        # print('The Dictionary: ')
        # print(pd_dictionary)
        data_frame = pd.DataFrame(pd_dictionary)

        self.export_data_frame(data_frame=data_frame)
        return data_frame

    def export_data_frame(self,data_frame):
        """Basically the reason for this function is to give the file name a random number
        this is simply to give each augmented dataset an almost unique key in the easiest way.
        """
        # Create the path to export the dataset to:
        today = date.today()
        file_name_str_no_csv = today.strftime("%b-%d-%Y") # Generate the date.
        random_key = str(random.randint(0, 100)) # Generate rhe random number.
        random_key_with_borders = '[' + random_key + ']' # Give the random key boarders to differentiate between the key and the date.
        file_name_str = file_name_str_no_csv + random_key_with_borders + '.csv' # Generate the file name str. 
        file_export = os.path.join(self.export_path, file_name_str)
        
        # Export the dataframe:
        data_frame.to_csv(file_export)

    def augment(self):
        df = self.df # Get the dataset.
        new_rows = [] # Store the augmented data.

        for row_index in range(0, (len(df.to_numpy()))):
            row = df.iloc[row_index] # Get the new row.

            # Now loop through the extended binary permutations:
            for x, combination in enumerate(self.combinations):
                holder = [] # Hold the augmented values.
                holder = self.apply_meta_data(row=row, combination=combination)

                # Loop through the row's values in groups of three:
                for i in range(0, len(self.values_2), 3):
                    v_1, v_2, v_3 = self.values_2[i:i+3]

                    # Augment the values:
                    value_01 = self.augment_value(value=row[str(v_1[0])], rule=v_1[1], operator=combination[0])
                    value_02 = self.augment_value(value=row[str(v_2[0])], rule=v_2[1], operator=combination[1])
                    value_03 = self.augment_value(value=row[str(v_3[0])], rule=v_3[1], operator=combination[2])

                    # Add to the holder:
                    holder.append(value_01)
                    holder.append(value_02)
                    holder.append(value_03)

                new_rows.append(holder)


        print('The augmentation should be done, so going to print a painful log')
        print(new_rows)
        new_data_frame = self.add_to_data_frame(new_rows=new_rows)
        print(new_data_frame)
        x = input('...')
    

















