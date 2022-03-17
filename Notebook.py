#%%

# Folders to delete:
# New Presets Json
# New Presets XML
# Training Presets

import os

json_export = os.path.join('NewPresetsJson')
xml_export = os.path.join('NewPresetsXML')
training_presets = os.path.join('TrainingData', 'TrainingPresets')

# JSON:
for f in os.listdir(json_export):
    os.remove(os.path.join(json_export, f))

#%% 
# XML:
for f in os.listdir(xml_export):
    os.remove(os.path.join(xml_export, f))
    
# Training:
for f in os.listdir(training_presets):
    os.remove(os.path.join(training_presets, f))
    
    
# %%
import pandas as pd
datasets_path = os.path.join('TrainingData', 'Datasets')

df = pd.read_csv(os.path.join(datasets_path, 'Mar-16-2022.csv'))
df.head()

# %%

"""
We are going to try and train the plucks brightness and Consistency values.
"""
"""
Data prep
"""

# gapminder.loc[,: ['country','year']].head()

print(df.columns)

# %%

selected_columns = df[['Consistency', 'Brightness', 'OscillatorDetune2', 'OscillatorDetune', 'FilterCutoffFrequency']]

# %%
selected_columns.head()
# %%

# Create a train and test set:
from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(selected_columns, test_size=0.1) 

train_df.head()


# %%
test_df.head()
# %%

# Create the model:

def neural_network_classifier(train, test, epochs):
    # Select values to create X and Y:
    train_x = train[['Alpha', 'Beta', 'Lambda','Lambda1', 'Lambda2']].to_numpy()
    test_x = test[['Alpha', 'Beta', 'Lambda','Lambda1', 'Lambda2']].to_numpy()
    
    train_y = train[['Labels']].to_numpy()
    test_y = test[['Labels']].to_numpy()
    
    # Reshape Y values:
    train_y = np.reshape(train_y, (-1, len(train_y)))
    train_y = train_y[0]
    
    test_y = np.reshape(test_y, (-1, len(test_y)))
    test_y = test_y[0]
    
    # Create neural network model: (Need a sigmoid function for hidden layers and a logistic function for the ouput)
    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=[5]),
        keras.layers.Dense(500, activation='sigmoid'),
        keras.layers.Dense(500, activation='sigmoid'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        loss='binary_crossentropy',
        optimizer='sgd',
        metrics=['accuracy']
    )     
    
    # Train the model:
    history = model.fit(train_x, train_y, epochs=epochs)
    
    # Present any metrics that it produces:
    history_df = pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()
    
    # Calculate the accuracy of the Neural network model:
    model_predicts = model.predict_classes(test_x)
    
    # Retreive the accuracy score of the Neural network:
    acc_score = accuracy_score(test_y, model_predicts)
    
    return acc_score


#%%
from tensorflow import keras
train_x = train_df[['Consistency']]
test_x = test_df[['Consistency']]

train_y = train_df[['OscillatorDetune2', 'OscillatorDetune']]
test_y = test_df[['Consistency', 'Brightness']]

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[1]),
    keras.layers.Dense(5, activation='relu'),
    keras.layers.Dense(2, activation='relu')
])

model.compile(
    loss='mean_squared_error',
    optimizer='sgd'
)

history = model.fit(train_x, train_y, epochs=10)

#%%

pred_df = model.predict(x=test_x)

# %%
print(pred_df)
# %%
