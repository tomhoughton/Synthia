# Imports:
import os
import pandas as pd
import platform
from datetime import date
import numpy as np
from SynthiaStats import SynthiaStats
import random

""" 
TODO:
- We need to create all of the rules that must be folled during the augmentation:
    - We must create a hyper parameter for the range of audible difference.
    - Some rules of the top of my head:
        - The detunes must be the same distance from 0.5 -> could augment one then calculate the distance
                                                            then subtract that distance from 0.5 to get the lower.
        - All augmentations must adhere to the min and max of the dataset to preserve the groups.
"""

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

        # this is a log to print at the end, I'm going to put all logs here:
        self.dev_log = []

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

        self.values = [
   #         ['OscillatorWaveShape', 'Preserve'],
    #        ['OscillatorOct', 'Preserve'],
     #       ['OscillatorSemi', 'Preserve'],
      #      ['OscillatorDetune', 'Consistency'],
       #     ['FilterCutoffFrequency', 'Brightness'],
        #    ['FilterLFOCutoffMod', 'Evolution'],
         #   ['FilterEnvCutoffMod', 'Dynamics'],
          #  ['LFOSpeed', 'Evolution'],
           # ['LFOFadeIn', 'Preserve'],
            #['OscillatorWaveShape2', 'Preserve'],
            #['OscillatorOct2', 'Preserve'],
            #['OscillatorSemi2', 'Preserve'],
            #['OscillatorDetune2', 'Consistency'],
            #['AttackTime', 'Type', 'Dynamics'],
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

    def set_descriptor_stats(self, consistency, dynamics, brightness, evolution):
        """
            The purpose of this function is to literally just set the statistics into the 
            global variables of this class. I just couldn't be botheres to edit the CLI.
        """

        # Set consistency:
        self.consistency_stats = consistency

        # Set dyamics:
        self.dynamics_stats = dynamics

        # Set brightness:
        self.brightness_stats = brightness

        # Set the evolution stats:
        self.evolution_stats = evolution


    def sort_min_max_stats_paths(self, descriptor_mmm_path):
        # We need to know what descriptor it is:
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
        
        # # Display the dfs:
        # for df in dfs:
        #     print(df)
        #     print('--------------------------------------------------------------')

        # x = input('...')

        # Return the sorted dataframes:
        return dfs

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

    def export_data_frame(self, data_frame):
        
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

        # Confirm the export:
        print('Dataset exported!!!')
        print('------------------------------')
        print('Name: ', file_name_str)
        print('Path: ', file_export)

    def apply_meta_data(self, row, combination):
        rtn = [] # This stores the list for the function to return.

        for m in self.meta:
            if m == 'Name':
                rtn.append(row[m] + "_" + str(combination))
            else:
                rtn.append(row[m])

        return rtn


    def augment_value(self, value, rule, operator):

        """
        TODO: We need to implement the range of audible difference in here
        TODO: We need to gather the min and max to help us know whether the new value fits within the range of the group.
        NOTE: In terms of operators [0 = -] [1 = None] [2 = +]
        """

        # NOTE: Need to find a better name for this variable as I know it's the wrong word for it.
        scalar = random.uniform(0, self.audible_difference_range)

        # We need to get the correct array:
        

        if (rule == "Preserve"):
            return value
        
        if (operator == 0): # -
            new_value = value - scalar

            # Now we need to check the min and max stats of this number.        

            return value - 1
        elif (operator == 1): # None
            return value
        elif (operator == 2): # + 
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

    def get_stats_per_feature(self, values, row):

        """ 
        What does this function need TODO:
            * We need to figure out the descriptor of it.
            * Then we need to get the degrees
            * Then return the min and max:


        Dev:
        TODO: Make sure it's getting the stats we need and not just one of the stats where for example all values aren't
        of the same descriptor.
        """
        
        print('Values', values)

        current_descriptor = values[2]

        # Lets get the descriptor of the current row:
        current_descriptor_degree = float(row[str(values[2])])

        # NOTE: May need to remove this.
        print('Current_descriptor degree: ', current_descriptor_degree)

        # We need to check to make sure that the value isn't a 1.0:
        if current_descriptor_degree == 1.0:
            current_descriptor_degree = int(current_descriptor_degree)
        else:
            current_descriptor_degree = int(current_descriptor_degree * 10)

        current_stats = []

        # We need to get the correct array:        
        if (current_descriptor == 'Consistency'):
            current_stats = self.consistency_stats
        elif (current_descriptor == 'Brightness'):
            current_stats = self.brightness_stats
        elif (current_descriptor == 'Evolution'):
            current_stats = self.evolution_stats
        elif (current_descriptor == 'Dynamics'):   
            current_stats = self.dynamics_stats

        stats = current_stats[current_descriptor_degree]

        # NOTE: May need to remove this.
        print('Returned stats: ')
        print(stats)
        print('Row: ')
        print(row)
        return stats 

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

            # print('------------------------ Row: ----------------------------------------------')
            # print(row)

            # Now loop through the augmentation combinations:
            for x, combination in enumerate(self.combinations):
                holder = [] # This stores the augmented values.

                # We need to apply the meta/descriptor data to the holder list.
                holder = self.apply_meta_data(row=row, combination=combination)

                # Loop through the augmentable values in groups of three:
                for i in range(0, len(self.values_2), 3):
                    v_1, v_2, v_3 = self.values_2[i:i+3]
                    
                    # We need to get the min max values per feature and descriptor:
                    self.get_stats_per_feature(values=v_1, row=row)
                    self.get_stats_per_feature(values=v_2, row=row)
                    self.get_stats_per_feature(values=v_3, row=row)

                    # Retrieve augmented values:
                    value_01 = self.augment_value(value=row[str(v_1[0])], rule=v_1[1], operator=combination[0])
                    value_02 = self.augment_value(value=row[str(v_2[0])], rule=v_2[1], operator=combination[1])
                    value_03 = self.augment_value(value=row[str(v_3[0])], rule=v_3[1], operator=combination[2])

                    holder.append(value_01)
                    holder.append(value_02)
                    holder.append(value_03)

                new_rows.append(holder)
            
            # NOTE: May need to remove this.
            x = input('-_- -_- -_-')
            # self.clear_console()
            # print('| ', row_index, ' / ', len(df.to_numpy()) - 1, '|')
            # counter += '#'
            # print(counter)

        new_data_frame = self.add_to_data_frame(new_rows=new_rows)

        # We need to confirm the data frame: 
