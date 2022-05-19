""" 
TASKS:
    - Import the dataset [X]
    - Encode the labeled data [X]
    - Filter out the columns that you need to create new dfs
    - Create a train and test set
    - Create the nn
    - Train it
"""




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

