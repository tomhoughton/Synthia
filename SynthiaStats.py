# Imports:
import pandas as pd

"""
THINGS TO DO:
- Display min and max for each descriptor in some way and create a save option to save all the datasets for progress.
- Make a function return the min and max of all the degrees in a dataset for the data augmentation code.
"""



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

You also need to save the data summary with the date.
and also make the display code easier to read.
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


    def type_count(self):

        print('████████╗██╗░░░██╗██████╗░███████╗  ░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗')
        print('╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝')
        print('░░░██║░░░░╚████╔╝░██████╔╝█████╗░░  ██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░')
        print('░░░██║░░░░░╚██╔╝░░██╔═══╝░██╔══╝░░  ██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░')
        print('░░░██║░░░░░░██║░░░██║░░░░░███████╗  ╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░')
        print('░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝  ░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░')

        rtn_dict = {}

        for s_type in self.types:
            rtn_dict[s_type] = [self.df['Type'].value_counts()[s_type]]

        rtn_df = pd.DataFrame(rtn_dict)
        print('')
        print('')
        print('')
        print(rtn_df)
        print('')
        print('')
        print('')


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
        print('')
        print('')
        print('')
        print('░█████╗░░█████╗░███╗░░░███╗██████╗░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗')
        print('██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║')
        print('██║░░╚═╝██║░░██║██╔████╔██║██████╦╝██║██╔██╗██║███████║░░░██║░░░██║██║░░██║██╔██╗██║')
        print('██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗██║██║╚████║██╔══██║░░░██║░░░██║██║░░██║██║╚████║')
        print('╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝██║██║░╚███║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║')
        print('░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝')

        print('░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗░██████╗')
        print('██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔════╝')
        print('██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░╚█████╗░')
        print('██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░░╚═══██╗')
        print('╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░██████╔╝')
        print('░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░')
        print('')
        print('')
        print('')
        combinations = self.get_combination_dfs()
        df_dict = {}

        for combination in combinations:
            data_frame = combination[0]
            combination_id = combination[1]
            c, r = data_frame.shape
            df_dict[combination_id] = [c]

        return pd.DataFrame(data=df_dict)


    def get_descriptor_degrees_min_max_mean(self):

        """This function is to generate the min and max for each column in accordance to the 
           description degrees to aid in generating new bits of data.
        """

        combinations = self.get_combination_dfs()

        # temp_df = combinations[0][0].copy() # This dataframe is just to test this idea.
        temp_df = self.df

        # # Table to summarise:
        # print('The table to summaries')

        # # Firstly we need to drop columns that really aren't necesarry:
        # temp_df = temp_df.drop(columns=['Consistent', 'Dynamic', 'Bright', 'Evolves'])

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

        # # Now we need to get the min and max of each dataframe:
        # consistency_min_max = self.get_min_max(data=temp_consistency_df)
        # dynamics_min_max = self.get_min_max(data=temp_dynamics_df)
        # brightness_min_max = self.get_min_max(data=temp_brightness_df)
        # evolution_min_max = self.get_min_max(data=temp_evolution_df)

        # print(consistency_min_max)
        # print(dynamics_min_max)
        # print(brightness_min_max)
        # print(evolution_min_max)

        # Lets try and do this for consistency:
        # FIX THIS CODE !!!!!! THE ISSUE IS WITH BRIGHTNESS
        
        # THIS IS THE CODE TO IMPROVE THIS FUNCTION: THE CODE ABOVE IS KEPT FOR REFERENCE!!!!
        # Firstly we need a df for each degree that exists in the df:

        # Consistency: 
        consistency_unqiue_values = temp_consistency_df.Consistency.unique()
        consistency_unique_dfs = self.get_unique_values_dfs(temp_consistency_df, consistency_unqiue_values, descriptor='Consistency')

        # Dynamics:
        dynamics_unique_values = temp_dynamics_df.Dynamics.unique()
        dynamics_unique_dfs = self.get_unique_values_dfs(data=temp_dynamics_df, values=dynamics_unique_values, descriptor='Dynamics')

        # Brightness:
        brightness_unique_values = temp_brightness_df.Brightness.unique()
        brightness_unique_dfs = self.get_unique_values_dfs(data=temp_brightness_df, values=brightness_unique_values, descriptor='Brightness')

        # Evolution:
        evolution_unique_values = temp_evolution_df.Evolution.unique()
        evolution_unique_dfs = self.get_unique_values_dfs(data=temp_evolution_df, values=evolution_unique_values, descriptor='Evolution')

        # Get min max for all degrees of each descriptor:
        consistency_min_max_mean_dfs = self.get_all_min_max(data_frames=consistency_unique_dfs)

        # Dynamics:
        dynamics_min_max_mean_dfs = self.get_all_min_max(data_frames=dynamics_unique_dfs)

        # Brightness:
        brightness_min_max_mean_dfs = self.get_all_min_max(data_frames=brightness_unique_dfs)

        # Evolution:
        evolution_min_max_mean_dfs = self.get_all_min_max(data_frames=evolution_unique_dfs)

        return consistency_min_max_mean_dfs, dynamics_min_max_mean_dfs, brightness_min_max_mean_dfs, evolution_min_max_mean_dfs

    def display_decriptor_stats(self, consistency, dynamics, brightness, evolution):
        print('')
        print('')
        print('')
        # Display consistency title:
        print('---------------------------------------------------------------------------------------')
        print('░█████╗░░█████╗░███╗░░██╗░██████╗██╗░██████╗████████╗███████╗███╗░░██╗░█████╗░██╗░░░██╗')
        print('██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝')
        print('██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║╚█████╗░░░░██║░░░█████╗░░██╔██╗██║██║░░╚═╝░╚████╔╝░')
        print('██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚████║██║░░██╗░░╚██╔╝░░')
        print('╚█████╔╝╚█████╔╝██║░╚███║██████╔╝██║██████╔╝░░░██║░░░███████╗██║░╚███║╚█████╔╝░░░██║░░░')
        print('░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░')
        print('---------------------------------------------------------------------------------------')

        # Display the graphs:
        for df in consistency:
            print('---------------------------------------------------------------------------------------')
            print(df)
            print('---------------------------------------------------------------------------------------')
            x = input('...')

        x = input('...')

        print('----------------------------------------------------------------')
        print('██████╗░██╗░░░██╗███╗░░██╗░█████╗░███╗░░░███╗██╗░█████╗░░██████╗')
        print('██╔══██╗╚██╗░██╔╝████╗░██║██╔══██╗████╗░████║██║██╔══██╗██╔════╝')
        print('██║░░██║░╚████╔╝░██╔██╗██║███████║██╔████╔██║██║██║░░╚═╝╚█████╗░')
        print('██║░░██║░░╚██╔╝░░██║╚████║██╔══██║██║╚██╔╝██║██║██║░░██╗░╚═══██╗')
        print('██████╔╝░░░██║░░░██║░╚███║██║░░██║██║░╚═╝░██║██║╚█████╔╝██████╔╝')
        print('╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚════╝░╚═════╝░')
        print('----------------------------------------------------------------')

        for df in dynamics:
            print('---------------------------------------------------------------------------------------')
            print(df)
            print('---------------------------------------------------------------------------------------')
            x = input('...')


        x = input('...')

        print('------------------------------------------------------------------------------')
        print('██████╗░██████╗░██╗░██████╗░██╗░░██╗████████╗███╗░░██╗███████╗░██████╗░██████╗')
        print('██╔══██╗██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝████╗░██║██╔════╝██╔════╝██╔════╝')
        print('██████╦╝██████╔╝██║██║░░██╗░███████║░░░██║░░░██╔██╗██║█████╗░░╚█████╗░╚█████╗░')
        print('██╔══██╗██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░██║╚████║██╔══╝░░░╚═══██╗░╚═══██╗')
        print('██████╦╝██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██║░╚███║███████╗██████╔╝██████╔╝')
        print('╚═════╝░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░')
        print('------------------------------------------------------------------------------')

        for df in brightness:
            print('---------------------------------------------------------------------------------------')
            print(df)
            print('---------------------------------------------------------------------------------------')
            x = input('...')
            print('')

        x = input('...')

        print('-----------------------------------------------------------------------')
        print('███████╗██╗░░░██╗░█████╗░██╗░░░░░██╗░░░██╗████████╗██╗░█████╗░███╗░░██╗')
        print('██╔════╝██║░░░██║██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║██╔══██╗████╗░██║')
        print('█████╗░░╚██╗░██╔╝██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██╔██╗██║')
        print('██╔══╝░░░╚████╔╝░██║░░██║██║░░░░░██║░░░██║░░░██║░░░██║██║░░██║██║╚████║')
        print('███████╗░░╚██╔╝░░╚█████╔╝███████╗╚██████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║')
        print('╚══════╝░░░╚═╝░░░░╚════╝░╚══════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝')
        print('-----------------------------------------------------------------------')

        for df in evolution:
            print('---------------------------------------------------------------------------------------')
            print(df)
            print('---------------------------------------------------------------------------------------')
            x = input('...')
            print('')

        x = input('...')
        














    def get_all_min_max(self, data_frames):
        rtn = []
        for df in data_frames:
            min_max_mean = self.min_max_descriptor(data_frame=df)
            rtn.append(min_max_mean)

        return rtn

    def min_max_descriptor(self, data_frame):

        """ 
        -- Title -- 
        Name   Min,  Max,  Mean
        Column
        Column
        Column
        """
        pd_dict = {}
        pd_dict['Name'] = []
        pd_dict['Min'] = []
        pd_dict['Max'] = []
        pd_dict['Mean'] = []

        for col_index, col in enumerate(data_frame[1:]):
            pd_dict['Name'].append(str(data_frame.columns[col_index]))
            pd_dict['Min'].append(data_frame[col].min())
            pd_dict['Max'].append(data_frame[col].max())
            pd_dict['Mean'].append(data_frame[col].mean())
        
        df = pd.DataFrame(data=pd_dict)
        return df
                

        
        
    def get_unique_values_dfs(self, data, values, descriptor):
        
        """This function will return dataframes where the descriptor column only contains the same value.
           This is to gain min and max values at each degree of the description.

        Returns:
            List of Pandas Data Frames: The list contains these unqiue dataframes.
        """

        data_frames = []
        for v in values:
            data_frames.append(data[data[descriptor] == v])

        return data_frames


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
        

        





    
        