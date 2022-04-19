# Imports:
import os
import pandas as pd
import platform
from datetime import date
import numpy as np
from SynthiaStats import SynthiaStats

""" 
TODO:
- We need to create all of the rules that must be folled during the augmentation:
    - Some rules of the top of my head:
        - The detunes must be the same distance from 0.5 -> could augment one then calculate the distance
                                                            then subtract that distance from 0.5 to get the lower.
        - All augmentations must adhere to the min and max of the dataset to preserve the groups.
"""

class Augmentor:
    
    def __init__(self, df, date) -> None:
        
        # Augmented Dataset export path:
        self.export_path = os.path.join('TrainingData', 'AugmentedDatasets')

        # We need to get dataset:
        self.df = df

        # Store the binary permutations for the augmentation algorithm:
        self.combinations = []
        
        # So we need to also read and obtain the directories of where the statistics are located:
        self.date_var = date # Store the date of the of the statistics that we'll use. 
        self.path_to_stats = os.path.join('Statistics', self.date_var)
        self.consistency_path = os.path.join(self.path_to_stats, 'ConsistencyMinMaxMean')
        self.brightness_path = os.path.join(self.path_to_stats, 'BrightnessMinMaxMean')
        self.dynamics_path = os.path.join(self.path_to_stats, 'DynamicsMinMaxMean')
        self.evolution_path = os.path.join(self.path_to_stats, 'EvolutionMixMaxMean')

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
        
        # The numerical values of each preset:
        self.values = [
            ['OscillatorWaveShape', 'Preserve'],
            ['OscillatorOct', 'Preserve'],
            ['OscillatorSemi', 'Preserve'],
            ['OscillatorDetune', 'Consistency'],
            ['FilterCutoffFrequency', 'Brightness'],
            ['FilterLFOCutoffMod', 'Evolution'],
            ['FilterEnvCutoffMod', 'Dynamics'],
            ['LFOSpeed', 'Evolution'],
            ['LFOFadeIn', 'Preserve'],
            ['OscillatorWaveShape2', 'Preserve'],
            ['OscillatorOct2', 'Preserve'],
            ['OscillatorSemi2', 'Preserve'],
            ['OscillatorDetune2', 'Consistency'],
            ['AttackTime', 'Type', 'Dynamics'],
            ['DecayTime', 'Dynamics'],
            ['SustainLevel', 'Dynamics'],
            ['SustainTime', 'Dynamics'],
            ['ReleaseTime', 'Dynamics'],
            ['AttackTime2', 'Type', 'Dynamics'],
            ['DecayTime2', 'Dynamics'],
            ['SustainLevel2', 'Dynamics'],
            ['SustainTime2', 'Dynamics'],
            ['ReleaseTime2', 'Dynamics'],
            ['VibratoSpeed', 'Consistency'],
            ['VibratoAmount', 'Consistency'],
            ['KeyboardUnison', 'Preserve'],
            ['KeyboardDetune', 'Consistency']
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

    def sort_min_max_stats_paths(self, descriptor_mmm_path):

        # Get the list of file names in the directory:
        mmm_files = os.listdir(descriptor_mmm_path)
        
        # Remove .csv and convert everything to floats:
        store = np.zeros(len(mmm_files)) # Store an empty array of zeros matching the length of the files.

        # Enumerate through the files, the file is the name and i is the index to access the array.
        for i, file in enumerate(mmm_files):
            # Remove .csv, convert to float and store in the array.
            store[i] = float(file[:3])

        # Now we bubble sort the array:
        # Get the length of the store array:
        n = len(store)

        # Traverse through the store values:
        for i in range(n-1):
            for j in range(0, n-i-1):
                # Swap is the initial element is greater than the next element:
                if (store[j] > store[j + 1]):
                    store[j], store[j + 1] = store[j + 1], store[j]

        dfs = []
        for s in store:
            df_name = str(s) + '.csv'
            df = pd.read_csv(os.path.join(descriptor_mmm_path, df_name))
            dfs.append(df)
        
        # Display the dfs:
        for df in dfs:
            print(df)
            print('--------------------------------------------------------------')

        x = input('...')

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

            for index, v in enumerate(self.values):
                pd_dictionary[v[0]].append(row_slice[index])


        data_frame = pd.DataFrame(pd_dictionary)
        self.export_data_frame(data_frame=data_frame)

        return data_frame


    def export_data_frame(self, data_frame):
        
        # Get the date of when the augmented dataset was created:
        today = date.today()

        # Get the date string:
        file_name_date_str = today.strftime("%b-%d-%Y") + '.csv'

        # Create the path to export the dataset to:
        file_export = os.path.join(self.export_path, file_name_date_str)
        
        # Export the dataframe:
        data_frame.to_csv(file_export)


    def apply_meta_data(self, row, combination):
        rtn = [] # This stores the list for the function to return.

        for m in self.meta:
            if m == 'Name':
                rtn.append(row[m] + "_" + str(combination))
            else:
                rtn.append(row[m])

        return rtn


    def augment_value(self, value, rule, operator):
        if (rule == "Preserve"):
            return value
        
        if (operator == 0):
            return value - 1
        elif (operator == 1):
            return value + 0
        elif (operator == 2):
            return value + 2
        
        return 69


    def clear_console(self):
        # Get the os that the user is using:
        usr_os = platform.system()

        if (usr_os == 'Darwin'):
            clear = lambda: os.system('clear')
            clear()
        elif (usr_os == 'Linux'):
            clear = lambda: os.system('clear')
            clear()
        elif (usr_os == 'Windows'):
            clear = lambda: os.system('cls')
            clear()

    def confirm_augment(self, data_frame):

        # Create a new Synthia Stats Object:
        S_Stats = SynthiaStats(data=data_frame, is_exporting=False)

        # Display the dataframe:
        S_Stats.display_dataframe()
        x = input('...')

        # Get the type count:
        S_Stats.type_count()
        x = input('...')

        # Get the binary combination counts:
        combination_counts = S_Stats.get_combination_counts()
        print(combination_counts)
        x = input('...')

        
        consistency_mmm, dynamics_mmm, brightness_mmm, evolution_mmm = S_Stats.get_descriptor_degrees_min_max_mean()
        
        S_Stats.display_decriptor_stats(consistency_mmm, dynamics_mmm, brightness_mmm, evolution_mmm)

        # Call the export function:
        S_Stats.export_statistics()

        user_input = input('Press any key to exit: ')



    def augment(self):
        # Get the dataset:
        df = self.df

        # Store the augmented rows:
        new_rows = []
        counter = '' # This is to store the loading bar string.

        # Loop in range of the rows of the dataset:
        for row_index in range(0, (len(df.to_numpy()))):
            # Get the row:
            row = df.iloc[row_index]

            # Now loop through the augmentation combinations:
            for x, combination in enumerate(self.combinations):
                holder = [] # This stores the augmented values.

                # We need to apply the meta/descriptor data to the holder list.
                holder = self.apply_meta_data(row=row, combination=combination)

                # Loop through the augmentable values in groups of three:
                for i in range(0, len(self.values), 3):
                    v_1, v_2, v_3 = self.values[i:i+3]

                    # Retrieve augmented values:
                    value_01 = self.augment_value(value=row[str(v_1[0])], rule=v_1[1], operator=combination[0])
                    value_02 = self.augment_value(value=row[str(v_2[0])], rule=v_2[1], operator=combination[1])
                    value_03 = self.augment_value(value=row[str(v_3[0])], rule=v_3[1], operator=combination[2])

                    holder.append(value_01)
                    holder.append(value_02)
                    holder.append(value_03)

                new_rows.append(holder)
            
            self.clear_console()
            print('| ', row_index, ' / ', len(df.to_numpy()) - 1, '|')
            counter += '#'
            print(counter)

        new_data_frame = self.add_to_data_frame(new_rows=new_rows)

        # We need some form of confirmation to show the new augmented dataset, lets get some statistics:
        self.confirm_augment(data_frame=new_data_frame)