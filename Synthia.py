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

def min_max(df):
    """
    We need to get the min and max of each column with continuous values:

    - OscillatorWaveShape
    - OscillatorOct
    - OscillatorSemi
    - OscillatorDetune
    - FilterCutoffFrequency
    - FilterLFOCutoffMod
    - FilterEnvCutoffMod
    - LFOSpeed
    - LFOFadeIn
    - VibratoSpeed
    - Vibrato Amount
    - KeyboardUnison
    - KeyboardUnisonToggle
    - KeyboardDetune

    """

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

    # MIN:
    min_dict = {}
    min_dict['Stat'] = ['Min']

    for col in continueous_cols:
        min_dict[col] = [df[col].min()]

    # Max:
    max_dict = {}
    max_dict['Stat'] = ['Max']

    for col in continueous_cols:
        max_dict[col] = [df[col].max()]

    # Create final dataframes:
    min_df = pd.DataFrame(data=min_dict)
    max_df = pd.DataFrame(data=max_dict)

    summary_df = pd.concat([min_df, max_df])
    print(summary_df)


# The program must concat all the datasets that we need:
def main():
    print('Hello World')

    df = data_merge()

    print('Df Columns: ', df.columns)

    min_max(df=df)



if __name__ == "__main__":
    main()