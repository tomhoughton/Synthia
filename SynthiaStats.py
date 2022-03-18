# Imports:
import pandas as pd

""" 
What do you want to know:
- I would like to see the count for each TYPE of sound [X]
- I would like to see the count for each binary combination [X]
- I would like to see individual tables for the binary combinations []
- I would like the min and max for each column in the binary combination tables []

    - We could either get the min and max for each binary combination according to each row
    - Or we could either get the min and max for each degree of the descriptor

""" 

"""
Things for next time:
whilst you have the min and max you still need to get the min and max for each degree of the descriptors,
how you do that is up to you, however I think that using the binary descriptions is not the way to go for this task.
However the binary descriptions are good to aid in making more training examples to make new data off.
"""

class SynthiaStats: 
    
    def __init__(self, data) -> None:
        self.df = data
        self.types = [
            'Pluck',
            'Bass'
        ]

    def display_dataframe(self):
        print(self.df)
        print(self.df.columns)

    def type_count(self):
        rtn_dict = {}

        for s_type in self.types:
            rtn_dict[s_type] = [self.df['Type'].value_counts()[s_type]]

        rtn_df = pd.DataFrame(rtn_dict)
        print(rtn_df)

    def get_combination_dfs(self):

        """This function gathers each descriptor combination according to binary values.

        Returns:
            2D List: Contains the dataframe and the id (combination) of each dataframe.
        """

        ffff = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == False) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == False)]
        ffft = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == False) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == True)]
        fftf = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == False) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == False)]
        
        ftff = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == True) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == False)]
        ftft = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == True) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == True)]
        fftf = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == False) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == False)]

        fttt = self.df.loc[(self.df['Consistent'] == False) & (self.df['Bright'] == True) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == True)]
        tfff = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == False) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == False)]
        tfft = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == False) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == True)]
        
        tftf = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == False) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == False)]
        tftt = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == False) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == True)]
        ttft = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == True) & (self.df['Evolves'] == False) & (self.df['Dynamic'] == True)]

        tttf = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == True) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == False)]
        tttt = self.df.loc[(self.df['Consistent'] == True) & (self.df['Bright'] == True) & (self.df['Evolves'] == True) & (self.df['Dynamic'] == True)]

        combinations = [ffff, ffft, fftf, ftff, ftft, fftf, fttt, tfff, tfft, tftf, tftt, ttft, tttf, tttt]

        combinationsV2 = [
            [ffff, 'FFFF'],
            [ffft, 'FFFT'],
            [fftf, 'FFTF'],
            [ftff, 'FTFF'],
            [ftft, 'FTFT'],
            [fftf, 'FFTF'],
            [fttt, 'FTTT'],
            [tfff, 'TFFF'],
            [tfft, 'TFFT'],
            [tftf, 'TFTF'],
            [tftt, 'TFTT'],
            [ttft, 'TTFT'],
            [tttf, 'TTTF'],
            [tttt, 'TTTT']
        ]

        return combinationsV2

    def get_combination_counts(self):
        combinations = self.get_combination_dfs()
        df_dict = {}

        for combination in combinations:
            data_frame = combination[0]
            combination_id = combination[1]
            c, r = data_frame.shape
            df_dict[combination_id] = [c]

        return pd.DataFrame(data=df_dict)

    def get_combination_min_max(self):

        """This function is to generate the min and max for each column in accordance to the 
           description degrees to aid in generating new bits of data.
        """

        combinations = self.get_combination_dfs()

        temp_df = combinations[0][0].copy() # This dataframe is just to test this idea.

        # Table to summarise:
        print('The table to summaries')

        # Firstly we need to drop columns that really aren't necesarry:
        temp_df = temp_df.drop(columns=['Consistent', 'Dynamic', 'Bright', 'Evolves'])

        # Next we need to get the values which relate to each degree
        # This involves getting a df containing the decriptor and the value which we THINK 
        # the NN will draw a relationship between.

        # Consistency:
        temp_consistency_df = temp_df[['Consistency', 'OscillatorDetune', 'OscillatorDetune2', 'KeyboardUnison', 'KeyboardUnisonToggle', 'VibratoAmount', 'VibratoSpeed']]
        
        # Dynamics" 
        temp_dynamics_df = temp_df[['Dynamics', 'AttackTime', 'AttackTime2', 'DecayTime', 'DecayTime2', 'SustainTime', 'SustainTime2', 'ReleaseTime', 'ReleaseTime2', 'FilterEnvCutoffMod']]

        # Brightness:
        temp_brightness_df = temp_df[['Brightness', 'FilterCutoffFrequency']]

        # Evolution:
        temp_evolution_df = temp_df[['Evolution', 'LFOSpeed', 'FilterLFOCutoffMod']]
        
        print(temp_consistency_df)
        print(temp_dynamics_df)
        print(temp_brightness_df)
        print(temp_evolution_df)

        # Now we need to get the min and max of each dataframe:
        consistency_min_max = self.get_min_max(data=temp_consistency_df)
        dynamics_min_max = self.get_min_max(data=temp_dynamics_df)
        brightness_min_max = self.get_min_max(data=temp_brightness_df)
        evolution_min_max = self.get_min_max(data=temp_evolution_df)

        print(consistency_min_max)
        print(dynamics_min_max)
        print(brightness_min_max)
        print(evolution_min_max)



    def get_min_max(self, data):
        """This generates a new dataframe containing the min, max and mean for the given dataset.

        Args:
            data (pandas dataframe): dataframe to generate min max and mean from.
        """

        # Initialise the dictionary:
        df_dict = {}
        df_dict['Stat Type'] = ['Min']
        df_dict['Stat Type'].append('Max')
        df_dict['Descriptor'] = [data.columns[0]]
        df_dict['Descriptor'].append('---')

        for c in data.columns[1:]:
            df_dict[c] = [data[c].min()]
            df_dict[c].append(data[c].max())
            
        return pd.DataFrame(data=df_dict)
        

        





    
        