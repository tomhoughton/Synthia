"""
This is the ACTUAL main file for the program 
"""
import os
import pandas as pd

"""Statistics and data prep"""
def data_merge():
    # We need to loop through the folders containing the csv and concat them to a DataFrame:
    # We need to open the first one into a dataframe then concat the rest in a loop

    # Path to the datasets:
    datasets_path = os.path.join('TrainingData', 'Datasets')
    dataset_csvs = os.listdir(datasets_path)

    # Get the initial dataset:
    initial_dataset = pd.read_csv(os.path.join(datasets_path, dataset_csvs[0]))
    dataset_csvs = dataset_csvs[1:] # Drop the initial dataset from the array.

    # Loop through the remmaining datasets:
    for csv in dataset_csvs:

        current_df = pd.read_csv(os.path.join(datasets_path, csv))
        initial_dataset = pd.concat([initial_dataset, current_df])

    return initial_dataset

def type_min_max_V2(df):
    """Thomas -> Think about what you want to know
        - I want to know the min and max of values for each type [X] 
        - I want to know the min and max of values for each type and descriptor [X]
    """

    # Firstly we need to see how many different types we have in the data set:
    types = df.Type.unique()
    df_by_type = [] # Store the dataframes selected by type.

    # Loop through the types and add that selected df to df_by_type
    for _type in types: 
        new_df = df.loc[df['Type'] == _type]
        df_by_type.append(new_df)

    # Get the min and max of each column by type and store in a list:
    min_max_dict_list = []
    for data in df_by_type:
        min_max_dict_list.append(min_max_v2(df=data, type=data['Type'].iloc[0]))

    # Store the created dataframes based on the list of dictionaries above:
    min_max_df_list = []
    for diction in min_max_dict_list:
        new_df = pd.DataFrame(diction)
        min_max_df_list.append(new_df)

    # Concat all the dataframes in the list and display it:
    rtn_df = pd.concat(min_max_df_list)
    print(rtn_df)

    # Now we need to get the min and max for each table:

def min_max_v2(df, type):
    continueous_cols = [
        'OscillatorWaveShape', 
        'OscillatorOct', 
        'OscillatorSemi', 
        'OscillatorDetune', 
        'FilterCutoffFrequency', 
        'FilterLFOCutoffMod', 
        'FilterEnvCutoffMod',
        'LFOSpeed',
        'LFOFadeIn',
        'VibratoSpeed',
        'VibratoAmount',
        'KeyboardUnison',
        'KeyboardUnisonToggle',
        'KeyboardDetune'
    ]

    print('DATAFRAME: ')
    print(df)

    print('Type: ')
    print(type)

    # Min: 
    min_dict = {}
    min_dict['Type'] = [type]
    min_dict['Stat'] = ['Min']

    for col in continueous_cols:
        min_dict[col] = [df[col].min()]

    # Max:
    max_dict = {}
    max_dict['Type'] = [type]
    max_dict['Stat'] = ['Max']

    for col in continueous_cols:
        max_dict[col] = [df[col].max()]

    return max_dict, min_dict


# The program must concat all the datasets that we need:
def main():
    print('Hello World')

    df = data_merge()

    print(df)

    type_min_max_V2(df=df)



if __name__ == "__main__":
    main()