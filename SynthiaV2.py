from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import pandas as pd
import os
import matplotlib.pyplot as plt

"""
What does this need:
- Train test split
- 

"""

def train_test(df):
    train_df, test_df = train_test_split(df, test_size=0.1)
    return train_df, test_df

def consistency_brightness(train, test):
    
    train_x = train[['Consistency', 'Brightness']].to_numpy()
    train_y = train[['OscillatorDetune2', 'OscillatorDetune', 'FilterCutoffFrequency']].to_numpy()
    
    test_x = test[['Consistency', 'Brightness']]
    
    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=[2]),
        keras.layers.Dense(4, activation='relu'),
        keras.layers.Dense(4, activation='relu'),
        keras.layers.Dense(3)
    ])
    
    model.compile(
        loss='mean_squared_error',
        optimizer='sgd' 
    )
    
    history = model.fit(train_x, train_y, epochs=30)
    
    # Create a history data frame:
    history_df = pd.DataFrame(history.history).plot(figsize=(8, 5))
    
    print('History DF')
    print(history_df)
    
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()
    
    
    predictions = model.predict(x=test_x)
    
    
    
    
    
    return predictions

def main():
    print('Hello World')
    
    datasets = os.path.join('TrainingData', 'Datasets')
    
    df = pd.read_csv(os.path.join(datasets, 'Mar-16-2022.csv'))
    print(df)
    
    train_df, test_df = train_test(df)
    
    print(train_df)
    print(test_df)
    
    predictions = consistency_brightness(train=train_df, test=test_df)
    
    print(predictions)
    
main()
    
