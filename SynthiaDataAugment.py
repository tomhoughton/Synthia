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
            'KeyboardUnison',
            'KeyboardUnisonToggle',
            'VibratoAmount',
            'VibratoSpeed'
        ]

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

        
    def augment_min_max(self, row):
        # The augment margin is just the degree at which we +/-
        # We need to create a variable to store the augmented peices of data.
        print(row['Name'])

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


        




    