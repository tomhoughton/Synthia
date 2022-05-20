
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
import json
import xmltodict
import gzip
    
class Synthia:
    def __init__(self, df) -> None:
        self.df = df
        self.model_export_path = os.path.join('Models') # Store the path to the export folder.
        # These are all of the columns/synth-parameters which were used to design the sounds for the training data,
        # and what the model will use to make it's own sounds. 
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
            'FilterCutoffFrequency',
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
            'FilterLFOCutoffMod',
            'FilterCutoffFrequency'
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
            'FilterLFOCutoffMod',
            'FilterCutoffFrequency'
        ]]

        model = keras.models.Sequential([
            keras.layers.Flatten(input_shape=[8]),
            keras.layers.Dense(15, activation='relu'),
            keras.layers.Dense(25, activation='relu'),
            keras.layers.Dense(15, activation='relu'),
            keras.layers.Dense(21)
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

        # Export the model:
        model.save(os.path.join(self.model_export_path, 'synthia.h5'))
        # print('Models saved')
        print('Input: ', test_x[0])
        print('Input: ', test_x[0].shape)

        print('Test')
        print(model.predict(x=np.array([[0.3, 0.5, 1.0, 0.7, 0.0, 0.0, 1.0, 0.0]])))

        print('Input: ', test_x[0])
        print('Input: ', test_x[0].shape)

        x = input('....')

    def predict(self, model):
        print('Get the predictions')

        # Get the trained neural network:
        models_path = os.path.join('Models')
        model = keras.models.load_model(os.path.join(models_path, 'synthia.h5'))
        
        # Get the input:
        input = [[0.3, 0.5, 1, 0.7, 1, 0, 0, 0]]
        prediction = model.predict(x=input) # Make the prediction.

        # Matrix of trained features and rules which must be follwed,
        # The rules are for some final data manipulation to allow it to work,
        # in Ableton.
        features = [
            ['OscillatorWaveShape', 'Round', 'SignalChain1', 'OscillatorWaveShape'],
            ['OscillatorWaveShape2','Round', 'SignalChain2', 'OscillatorWaveShape'],
            ['OscillatorOct','Round', 'SignalChain1', 'OscillatorOct'],
            ['OscillatorOct2','Round', 'SignalChain2', 'OscillatorOct'],
            ['OscillatorDetune','Leave', 'SignalChain1', 'OscillatorDetune'],
            ['OscillatorDetune2','Leave', 'SignalChain2', 'OscillatorDetune'],
            ['VibratoAmount','Leave', 'Global', 'VibratoAmount'],
            ['VibratoSpeed','Leave', 'Global', 'VibratoSpeed'],
            ['KeyboardDetune','Leave', 'Global', 'KeyboardDetune'],
            ['AttackTime','Leave', 'Envelope.0', 'AttackTime'],
            ['AttackTime2','Leave', 'Envelope.1', 'AttackTime'],
            ['DecayTime','Leave', 'Envelope.0', 'DecayTime'],
            ['DecayTime2','Leave', 'Envelope.1', 'DecayTime'],
            ['SustainTime','Leave', 'Envelope.0', 'SustainTime'],
            ['SustainTime2','Leave', 'Envelope.1', 'SustainTime'],
            ['ReleaseTime','Leave', 'Envelope.0', 'ReleaseTime'],
            ['ReleaseTime2','Leave', 'Envelope.1', 'ReleaseTime'],
            ['FilterEnvCutoffMod','Leave', 'SignalChain1', 'FilterEnvCutoffMod'],
            ['LFOSpeed','Leave', 'SignalChain1', 'SignalChain1', 'LFOSpeed'],
            ['FilterLFOCutoffMod','Leave', 'SignalChain1', 'FilterLFOCutoffMod'],
            ['FilterCutoffFrequency', 'Leave', 'SignalChain1', 'FilterCutoffFrequency']
        ]

        features_2d = [] # This will hold the features values and features name:

        for i, value in enumerate(prediction[0]):
            val = 0
            
            if (features[i][1] == 'Round'):
                val = round(value)
            else:
                val = value

            features_2d.append([features[i][0], val])

        return features_2d


    def export_preset(self, synthia_output):
        """This function will allow the exporting of the synthia predicted presets
        into ableton.

        Args:
            synthia_output (2D array): This is the features_2d (return value) of predict function.
        """
        
        print('Export Preset')

        synthia_artefacts_path = os.path.join('SynthiaArtefacts')
        data = self.populate_genesis(features_2d=synthia_output)

        # Now we need to convert the json to xml:



    def populate_genesis(self, features_2d):
        """This function is to essentially populate a .json variation of Ableton Presets.
        """

        new_presets_json_path = os.path.join('NewPresetsJson')
        synthia_artefacts_path = os.path.join('SynthiaArtefacts')
        new_presets_json_list = os.listdir(new_presets_json_path)
        genesis = os.path.join(new_presets_json_path, new_presets_json_list[0])

        with open(genesis) as json_file:
            data = json.load(json_file)

            # Global Values:
            data["Ableton"]["UltraAnalog"]["VibratoAmount"]["Manual"]["@Value"] = features_2d[6][1]
            data["Ableton"]["UltraAnalog"]["VibratoSpeed"]["Manual"]["@Value"] = features_2d[7][1]
            data["Ableton"]["UltraAnalog"]["KeyboardDetune"]["Manual"]["@Value"] = features_2d[8][1]
            
            # SignalChain1 values:
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorWaveShape"]["Manual"]["@Value"] = features_2d[0][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorOct"]["Manual"]["@Value"] = features_2d[2][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorDetune"]["Manual"]["@Value"] = features_2d[4][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterCutoffFrequency"]["Manual"]["@Value"] = features_2d[20][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterLFOCutoffMod"]["Manual"]["@Value"] = features_2d[19][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOSpeed"]["Manual"]["@Value"] = features_2d[18][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterEnvCutoffMod"]["Manual"]["@Value"] = features_2d[17][1]

            # SignalChain2 values:
            data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorWaveShape"]["Manual"]["@Value"] = features_2d[1][1]
            data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorOct"]["Manual"]["@Value"] = features_2d[3][1]
            data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorDetune"]["Manual"]["@Value"] = features_2d[5][1]

            # Envelope.0 values:
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["AttackTime"]["Manual"]["@Value"] = features_2d[9][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["DecayTime"]["Manual"]["@Value"] = features_2d[11][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["SustainTime"]["Manual"]["@Value"] = features_2d[13][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["ReleaseTime"]["Manual"]["@Value"] = features_2d[15][1]

            # Envelope.1 values:
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["AttackTime"]["Manual"]["@Value"] = features_2d[10][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["DecayTime"]["Manual"]["@Value"] = features_2d[12][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["SustainTime"]["Manual"]["@Value"] = features_2d[14][1]
            data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["ReleaseTime"]["Manual"]["@Value"] = features_2d[16][1]
            
            print('The data type: ', type(data))

            print('00000000000000000000000000000000')
            xml = xmltodict.unparse(data)
            print(xml)

            self.write_preset(os.path.join(synthia_artefacts_path, f"hello.adv"), xml)
        return data


    def write_preset(self, file_path, data):
        with gzip.open(file_path, 'w') as output:
            output.write(data.encode("utf-8"))

""" 
write_zipped_preset(os.path.join(path, f"{name}.adv"), xml)


    Utility for writing final preset content as zip file
    with gzip.open(file_path, "wb") as zip_handle:
        zip_handle.write(content.encode("utf-8"))

"""
