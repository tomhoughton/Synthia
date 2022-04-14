from SynthiaStats import SynthiaStats
import pandas as pd
import numpy as np

""" 
TODO: 
- Need to get the datasets of each entry for each degree of the descriptor []

"""


"""
How is this going to work?

- We are going to get the dataset and the stat summaries of it all.
"""

"""
Possible methods to augment data:
- Preserve min and max
- Preserve Min Mean and Max

"""

class DataAugmentor:
    def __init__(self, data, consistency, dynamics, brightness, evolution) -> None:
        self.df = data

        # These tables contain the min, mean and max.
        self.stats_consistency = consistency
        self.stats_brightness = brightness
        self.stats_dynamics = dynamics
        self.stats_evolution = evolution

        # We need to create arrays to store the values which are assosiated with each descriptor:
        self.consistency_features = [
            'Consistency', 
            'Consistent', 
            'OscillatorDetune', 
            'OscillatorDetune2', 
            'KeyboardDetune',
            'KeyboardUnisonToggle',
            'VibratoAmount',
            'VibratoSpeed'
        ]

        # self.consistency_features = [
        #     'Consistency', 
        #     'Consistent', 
        #     'OscillatorDetune', 
        #     'OscillatorDetune2', 
        #     'KeyboardUnison',
        #     'KeyboardUnisonToggle',
        #     'VibratoAmount',
        #     'VibratoSpeed'
        # ]

        self.dynamics_features = [
            'Dynamics',
            'Dynamic',
            'AttackTime',
            'AttackTime2',
            'DecayTime',
            'DecayTime2',
            'SustainTime',
            'SustainTime2',
            'ReleaseTime',
            'ReleaseTime2',
            'FilterEnvCutoffMod'
        ]

        self.evolution_features = [
            'Evolution',
            'Evolves',
            'LFOSpeed',
            'FilterLFOCutoffMod'
        ]

        self.brightness_features = [
            'Brightness',
            'Bright',
            'FilterCutoffFrequency'
        ]

        # Combination store:
        self.combinations = [] # This is a global class variable for the recursion algorithm to access.


    def display_current_working_data(self):
        print('Data Augment Display')
        print(self.df)
        print('--------------------------------------------------------------------------------')
        print(self.stats_brightness)
        print('--------------------------------------------------------------------------------')
        print(self.stats_consistency)


    def get_statistics(self):
        S_Stats = SynthiaStats(data=self.df, is_exporting=False)
        consistency_mmm, dynamics_mmm, brightness_mmm, evolution_mmm = S_Stats.get_descriptor_degrees_min_max_mean()

        for i in consistency_mmm:
            print('-----------------------------')
            print(consistency_mmm)

    def display_dataset(self):
        print('The Dataset')
        print(self.df)

    def get_individual_descriptors(self):
        # Consistency:
        temp_consistency_df = self.df[['Consistency', 'OscillatorDetune', 'OscillatorDetune2', 'KeyboardUnison', 'KeyboardUnisonToggle', 'VibratoAmount', 'VibratoSpeed']]
        
        # Dynamics" 
        temp_dynamics_df = self.df[['Dynamics', 'AttackTime', 'AttackTime2', 'DecayTime', 'DecayTime2', 'SustainTime', 'SustainTime2', 'ReleaseTime', 'ReleaseTime2', 'FilterEnvCutoffMod']]

        # Brightness:
        temp_brightness_df = self.df[['Brightness', 'FilterCutoffFrequency']]

        # Evolution:
        temp_evolution_df = self.df[['Evolution', 'LFOSpeed', 'FilterLFOCutoffMod']]

    """
    Binary Combinations:
    """

    def gen(self, n, arr, i):
        if i == n:
            rtn_arr = self.extract(arr, n, i)
            self.combinations.append(rtn_arr)

        # First assign "0" at the position and try for all other permutations.
        arr[i] = 0
        self.gen(n, arr, i + 1)

        # Assign "1" at the position and try for all other permutations.
        arr[i] = 1
        self.gen(n, arr, i + 1)

        # Assign "2" at the position and try for all other permutations.
        arr[i] = 2
        self.gen(n, arr, i + 1)

    def extract(self, arr, n, i):
        temp = []
        for i in range(0, n):
            temp.append(arr[i])

        return temp

    def generate_combinations(self, n):
        arr = [None] * n
        self.gen(n, arr, 0)

        print('Generate Combimations')
        rtn = np.array(self.combinations)
        print(rtn)


    # def buildArray(arr, n, i):
    #     temp = []
    #     for i in range(0, n):
    #         temp.append(arr[i])

    # def generateAllCombinations(n, arr, i):
    #     if i == n:
    #         rtn_arr = 

    def gen_augment_combinations():
        """
        This function will gather all combinations of increase, decrease and remmain whilst augmenting the data.
        This allows us to generate much more data.
        """

    def augmentable_features(self, row_dict):
        features = [
            'OscillatorWaveShape',
            'OscillatorOct',
            'OscillatorSemi',
            'OscillatorDetune',
            'FilterCutoffFrequency',
            'FilterLFOCutoffMod',
            'FilterEnvCutoffMod',
            'LFOSpeed',
            'LFOFadeIn',
            'OscillatorWaveShape2',
            'OscillatorOct2',
            'OscillatorSemi2',
            'OscillatorDetune2',
            'AttackTime',
            'DecayTime',
            'SustainLevel',
            'SustainTime',
            'ReleaseTime',
            'ReleaseTime',
            'AttackTime2',
            'DecayTime2',
            'SustainLevel2',
            'SustainTime2',
            'ReleaseTime2',
            'VibratoSpeed',
            'VibratoAmount',
            'KeyboardDetune'
        ]

        rtn_arr = np.ones(len(features))

        for index, feature in enumerate(features):
            rtn_arr[index] = float(row_dict[feature])

        return rtn_arr, features

    def non_augmentable_features(self, row_dict):
        features = [
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

        rtn_arr = np.ones(len(features))

        for index, feature in enumerate(features):
            rtn_arr[index] = feature
        
        return rtn_arr, features



    def augment_min_max(self, row):

        """
        This function augments a single row and will return a new dataframe or matrix of the new rows (discluding the original)
        """

        # The augment margin is just the degree at which we +/-
        # We need to create a variable to store the augmented peices of data.
        print(row)

        # get the augmentable features and non augmentable fewaures and non augmentable features:
        augmentable, augmentable_features = self.augmentable_features(row_dict=row)
        # non_augmentable, non_augmentable_features = self.non_augmentable_features(row_dict=row)

        # Get the amount of combinations for the augmentable features:
        self.generate_combinations(n = len(augmentable))

        # We need to get the values for each descriptor in each row before we augment.
        consistency_features = self.get_features_from_dict(row=row, descriptor='Consistency')
        # dynamics_features = self.get_features_from_dict(row=row, descriptor='Dynamics')
        # brightness_features = self.get_features_from_dict(row=row, descriptor='Brightness')
        # evolution_features = self.get_features_from_dict(row=row, descriptor='Evolution')

        # Now we need to get the min and max for each column and descriptor:
        # We need to somehow deicde how to select the descriptor stats based on the degree:

        # Get the stats:
        # consistency_mmm, dynamics_mmm, brightness_mmm, evolution_mmm = S_Stats.get_descriptor_degrees_min_max_mean()

        print('Consistency Features')
        
        print(consistency_features)
        print('Len: ', len(consistency_features))

        print('Combinations')
        
        

    def get_features_from_dict(self, row, descriptor):
        features = []
        
        if (descriptor == 'Consistency'):
            features = self.consistency_features
        elif (descriptor == 'Dynamics'):
            features = self.dynamics_features
        elif (descriptor == 'Brightness'):
            features = self.brightness_features
        elif (descriptor == 'Evolution'):
            features = self.evolution_features
        
        rtn_vector = np.ones(len(features))

        for feature_index, feature in enumerate(features):
            print('ISSUE')
            print('Feature: ', feature)
            print('Feature Value: ', row[feature])
            rtn_vector[feature_index] = row[feature]

        return rtn_vector


    def augment(self, method, margin):


        """
        This method will consist of going through each row of the dataset to augment it in every way possible.

        The new augmented rows will have a special key added to the name to differentiate between real and fake data
        entries.
            - We will use the min and max to constrain the new augmented data to ensure there is noo overlap,
              and that the patterns/trends created in the real dataset are preserved in the augmented dataset.

        The augmented rows will be added to a matrix/dataframe where at the end the two dataframes will be concatted
        into a new data frame and then stored in the augmented dataframes folder (doesn't exist yet)

        """

        # First step is to get the dataset: 
        data = self.df
        data = data.drop("Unnamed: 0", axis=1)
        data_reset_index = data.reset_index()
        

        """NEED TO FINISH THIS"""
        
        print('AUGMENT')
        
        for (index_label, row_series) in data.iterrows(): # Itertuples is used due to it being faster.
            self.augment_min_max(row=row_series.to_dict())
            # print(row_series.to_dict())            


        




    