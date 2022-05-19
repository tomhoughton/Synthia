
# Imports:
import pandas as pd
import os
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
    
class Synthia:
    def __init__(self, df) -> None:
        self.df = df
        self.relavant_columns = [
            'Consistency',
            'Brightness',
            'Evolution',
            'Dynamics',
            'OscillatorWaveShape',
            'OscillatorWaveShape2',
            'OscillatorOct',
            'OscillatorOct2',
            'OscillatorDetune',
            'OscillatorDetune2',
            'VibratoAmount',
            'VibratoSpeed',
            'KeyboardDetune',
            'AttackTime',
            'AttackTime2',
            'DecayTime',
            'DecayTime2',
            'SustainTime',
            'SustainTime2',
            'ReleaseTime',
            'ReleaseTime2',
            'FilterEnvCutoffMod',
            'LFOSpeed',
            'FilterLFOCutoffMod',
            'Type_Cat',
            0,
            1,
            2,
            3
        ]

    def encode_df(self):
        
        df = self.df.copy() # Create the df instance.
        
        print('ENcode DF')
        print(df)

        # Start label encoding:        
        label_encode = LabelEncoder() # Create a new Label Encoder.
        df['Type_Cat'] = label_encode.fit_transform(df['Type']) # Encode the Type column.

        # Star one hot encoding:
        onehot = OneHotEncoder(handle_unknown='ignore')
        one_hot_df = pd.DataFrame(
            onehot.fit_transform(df[['Type_Cat']]).toarray()
        )

        df = df.join(one_hot_df)
        print(df)
        return df

    def train(self):
        new_df = self.encode_df() # Encode the dataframe.

        # Now we need to filter out the columns that we need for training.
        filtered_df = new_df[self.relavant_columns].copy()
        print('Columns: ', filtered_df.columns)
        
        # Now we need to create the  train and test set:
        train_df, test_df = train_test_split(filtered_df, test_size=0.1)

        # Show to the train test split:
        print('TRAIN')
        print(train_df)
        print('----------------------------')
        print('TEST')
        print(test_df)

       
        # Start training the neural network:

        # Network inputs (x):
        train_x = train_df[['Consistency', 'Brightness', 'Evolution', 'Dynamics', 0, 1, 2, 3]].to_numpy()
        test_x = test_df[['Consistency', 'Brightness', 'Evolution', 'Dynamics', 0, 1, 2, 3]].to_numpy()

        # Network outputs (y):
        train_y = train_df[[
            'OscillatorWaveShape', 
            'OscillatorWaveShape2',
            'OscillatorOct',
            'OscillatorOct2',
            'OscillatorDetune',
            'OscillatorDetune2',
            'VibratoAmount',
            'VibratoSpeed',
            'KeyboardDetune',
            'AttackTime',
            'AttackTime2',
            'DecayTime',
            'DecayTime2',
            'SustainTime',
            'SustainTime2',
            'ReleaseTime',
            'ReleaseTime2',
            'FilterEnvCutoffMod',
            'LFOSpeed',
            'FilterLFOCutoffMod'
        ]]

        # Network outputs (y):
        test = test_df[[
            'OscillatorWaveShape', 
            'OscillatorWaveShape2',
            'OscillatorOct',
            'OscillatorOct2',
            'OscillatorDetune',
            'OscillatorDetune2',
            'VibratoAmount',
            'VibratoSpeed',
            'KeyboardDetune',
            'AttackTime',
            'AttackTime2',
            'DecayTime',
            'DecayTime2',
            'SustainTime',
            'SustainTime2',
            'ReleaseTime',
            'ReleaseTime2',
            'FilterEnvCutoffMod',
            'LFOSpeed',
            'FilterLFOCutoffMod'
        ]]

        model = keras.models.Sequential([
            keras.layers.Flatten(input_shape=[8]),
            keras.layers.Dense(15, activation='relu'),
            keras.layers.Dense(25, activation='relu'),
            keras.layers.Dense(15, activation='relu'),
            keras.layers.Dense(20)
        ])

        model.compile(
            loss='mean_squared_error',
            optimizer='sgd'
        )

        history = model.fit(train_x, train_y, epochs=60)

        # Create a history data frame:
        history_df = pd.DataFrame(history.history).plot(figsize=(8, 5))

        print('History DF')
        print(history_df)

        plt.grid(True)
        plt.show()

        predictions = model.predict(x=test_x)
        print(predictions)
        x = input('....')

