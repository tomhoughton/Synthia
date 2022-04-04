from SynthiaStats import SynthiaStats
import pandas as pd

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


    def display_current_working_data(self):
        print('Data Augment Display')
        print(self.df)
        print('--------------------------------------------------------------------------------')
        print(self.stats_brightness)
        print('--------------------------------------------------------------------------------')
        print(self.stats_consistency)


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

        
    def augment_min_max(self, augment_margin):
        # The augment margin is just the degree at which we +/-
        # We need to create a variable to store the augmented peices of data.

        

    # We need to create a function to augment each row to simplify the code


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

        for row in self.df.itertuples(): # Itertuples is used due to it being faster.
            
            # Do the augmentation method here:
            self.augment_min_max(augment_margin=margin)


        




    