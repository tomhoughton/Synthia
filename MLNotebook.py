""" 
TASKS:
    - Import the dataset [X]
    - Encode the labeled data [X]
    - Filter out the columns that you need to create new dfs
    - Create a train and test set
    - Create the nn
    - Train it
"""

# FilterCutoffFrequency


#%%
import pandas as pd
import os
augmented_path = os.path.join('TrainingData', 'AugmentedDatasets') # Path to the dataset.

df = pd.read_csv(os.path.join(augmented_path, 'May-18-2022[100].csv'))
df.head()
# %%

import numpy as np
from sklearn.preprocessing import LabelEncoder
# Right so we need to encode the labelled data

label_encode = LabelEncoder()

# Assign the numerical values and store them in a new column:
df['Type_Cat'] = label_encode.fit_transform(df['Type'])
print(df['Type_Cat'])

# %%

# One-hot Encoding:
from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder(handle_unknown='ignore')

# Reshape the category array into a 2D array:
one_hot_df = pd.DataFrame(
    onehot.fit_transform(df[['Type_Cat']]).toarray()
)

# Merge with the main df:
df = df.join(one_hot_df)
df.head()


#%%


# We need to make sure we know exactly what columns I'll be using to train it with:
print(df.columns)

relavant_columns = [
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

filtered_df = df[relavant_columns].copy()
filtered_df.head()

# %%
from sklearn.model_selection import train_test_split

train_df, test_df = train_test_split(df, test_size=0.1)

#%%
import tensorflow as tf
from tensorflow import keras
import numpy as np 

models_path = os.path.join('Models')
model = keras.models.load_model(os.path.join(models_path, 'synthia.h5'))

print(model.weights)

#[0.3 0.5 1.  0.7 0.  0.  1.  0. ]

input = [[0.3, 0.5, 1, 0.7, 1, 0, 0, 0]]

prediction = model.predict(x=input)
print(prediction)
# %%

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



features_2d = []

for i, value in enumerate(prediction[0]):
    val = 0
    if (features[i][1] == 'Round'):
        val = round(value)
    else:
        val = value


    print('Index: ', i, ': ', features[i][0], ': ', val, 'Rule: ', features[i][1])

    features_2d.append([features[i][0], val])

print('---------------------')
print(features_2d)


# %%

import os

synthia_artefacts_path = os.path.join('SynthiaArtefacts')
new_presets_json_path = os.path.join('NewPresetsJson')

new_presets_json_path_list = os.listdir(new_presets_json_path)

genesis = os.path.join(new_presets_json_path, new_presets_json_path_list[0])
print(genesis)


# %%
import json
# Now we need to read the json:
# Need to load the json file:


with open(genesis) as json_file:
    data = json.load(json_file)
    #data = set_globals(data=data)

    # Using loops to place the values into json doesn't work,
    # So we are going to have to do it manually.

    # Global Values:
    data["Ableton"]["UltraAnalog"]["VibratoAmount"]["Manual"]["@Value"] = features_2d[6][1]
    data["Ableton"]["UltraAnalog"]["VibratoSpeed"]["Manual"]["@Value"] = features_2d[7][1]
    data["Ableton"]["UltraAnalog"]["KeyboardDetune"]["Manual"]["@Value"] = features_2d[8][1]

    print(data["Ableton"]["UltraAnalog"]["VibratoAmount"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["VibratoSpeed"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["KeyboardDetune"]["Manual"]["@Value"])

    # SignalChain1 Values:
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorWaveShape"]["Manual"]["@Value"] = features_2d[0][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorOct"]["Manual"]["@Value"] = features_2d[2][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorDetune"]["Manual"]["@Value"] = features_2d[4][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterCutoffFrequency"]["Manual"]["@Value"] = features_2d[20][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterLFOCutoffMod"]["Manual"]["@Value"] = features_2d[19][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOSpeed"]["Manual"]["@Value"] = features_2d[18][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterEnvCutoffMod"]["Manual"]["@Value"] = features_2d[17][1]

    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorWaveShape"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorOct"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorDetune"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterCutoffFrequency"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterLFOCutoffMod"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOSpeed"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterEnvCutoffMod"]["Manual"]["@Value"])

    
    # SignalChain2 Values:
    data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorWaveShape"]["Manual"]["@Value"] = features_2d[1][1]
    data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorOct"]["Manual"]["@Value"] = features_2d[3][1]
    data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorDetune"]["Manual"]["@Value"] = features_2d[5][1]

    print(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorWaveShape"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorOct"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorDetune"]["Manual"]["@Value"])

    # Envelope.0 Values:
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["AttackTime"]["Manual"]["@Value"] = features_2d[9][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["DecayTime"]["Manual"]["@Value"] = features_2d[11][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["SustainTime"]["Manual"]["@Value"] = features_2d[13][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["ReleaseTime"]["Manual"]["@Value"] = features_2d[15][1]

    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["AttackTime"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["DecayTime"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["SustainTime"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["ReleaseTime"]["Manual"]["@Value"])

    # Envelope.1 Values:
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["AttackTime"]["Manual"]["@Value"] = features_2d[10][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["DecayTime"]["Manual"]["@Value"] = features_2d[12][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["SustainTime"]["Manual"]["@Value"] = features_2d[14][1]
    data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["ReleaseTime"]["Manual"]["@Value"] = features_2d[16][1]

    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["AttackTime"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["DecayTime"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["SustainTime"]["Manual"]["@Value"])
    print(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["ReleaseTime"]["Manual"]["@Value"])



#%%

    for i, f in enumerate(features):
        signal_chain = f[2]
        synthia_feature = f[0]
        ableton_feature = f[3]
        value = features_2d[i]

        print('#')
        print(synthia_feature, ': ', str(value[1]))
        print(signal_chain)
        print(ableton_feature)
        print('#')

        if (signal_chain == 'SignalChain1'):
            #print('SC1')
            #data["Ableton"]["UltraAnalog"]["SignalChain1"]

            try:
                data["Ableton"]["UltraAnalog"]["SignalChain1"][ableton_feature]["Manual"]["@Value"] = value[1]
            except KeyError:
                data["Ableton"]["UltraAnalog"]["SignalChain1"][ableton_feature]["Manual"] = value[1]

        elif (signal_chain == 'SignalChain2'):
    #        print('SC2')
    #        data["Ableton"]["UltraAnalog"]["SignalChain2"]

            try:
                data["Ableton"]["UltraAnalog"]["SignalChain2"][ableton_feature]["Manual"]["@Value"] = value[1]
            except KeyError:
                data["Ableton"]["UltraAnalog"]["SignalChain2"][ableton_feature]["Manual"] = value[1]

        elif (signal_chain == 'Global'):
            #print('Global')
            #data["Ableton"]["UltraAnalog"][""]

            try:
                data["Ableton"]["UltraAnalog"][ableton_feature]["Manual"]["@Value"] = value[1]
            except KeyError:
                data["Ableton"]["UltraAnalog"][ableton_feature]["Manual"] = value[1]

#%%
""" 

OscillatorWaveShape '1' = SignalChain1 -> OscillatorWaveShape
OscillatorWaveShape2 = SignalChain2 -> OscillatorWaveShape
OscillatorOct = SignalChain1 -> OscillatorOct
OscillatorOct2 = SignalChain2 -> OscillatorOct
OscillatorDetune = SignalChain -> OscillatorDetune
OscillatorDetune2 = SignalChain2 -> OscillatorDetune
VibratoAmount 



"""

for i, f in enumerate(features):
    signal_chain = f[2]
    synthia_feature = f[0]
    ableton_feature = f[3]
    value = features_2d[i]

    print('#')
    print(synthia_feature, ': ', str(value[1]))
    print(signal_chain)
    print(ableton_feature)
    print('#')

    if (signal_chain == 'SignalChain1'):
        #print('SC1')
        #data["Ableton"]["UltraAnalog"]["SignalChain1"]

        try:
            data["Ableton"]["UltraAnalog"]["SignalChain1"][ableton_feature]["Manual"]["@Value"] = value[1]
        except KeyError:
            data["Ableton"]["UltraAnalog"]["SignalChain1"][ableton_feature]["Manual"] = value[1]

    elif (signal_chain == 'SignalChain2'):
#        print('SC2')
#        data["Ableton"]["UltraAnalog"]["SignalChain2"]

        try:
            data["Ableton"]["UltraAnalog"]["SignalChain2"][ableton_feature]["Manual"]["@Value"] = value[1]
        except KeyError:
            data["Ableton"]["UltraAnalog"]["SignalChain2"][ableton_feature]["Manual"] = value[1]

    elif (signal_chain == 'Global'):
        #print('Global')
        #data["Ableton"]["UltraAnalog"][""]

        try:
            data["Ableton"]["UltraAnalog"][ableton_feature]["Manual"]["@Value"] = value[1]
        except KeyError:
            data["Ableton"]["UltraAnalog"][ableton_feature]["Manual"] = value[1]

print(data)



# %%







# %%
