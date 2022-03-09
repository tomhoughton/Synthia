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

# The program must concat all the datasets that we need:
def main():
    print('Hello World')

    df = data_merge()



if __name__ == "__main__":
    main()