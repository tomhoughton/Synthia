import pandas as pd
import os

# IMPORTANT VARIABLES:
meta = ['Name', 'KeyboardUnisonToggle']

values = [
    ['OscillatorWaveShape', 'Preserve'],
    ['OscillatorOct', 'Preserve'],
    ['OscillatorSemi', 'Preserve'],
    ['OscillatorDetune', 'Consistency'],
    ['FilterCutoffFrequency', 'Brightness'],
    ['FilterLFOCutoffMod', 'Evolution'],
    ['FilterEnvCutoffMod', 'Dynamics'],
    ['LFOSpeed', 'Evolution'],
    ['LFOFadeIn', 'Preserve'],
    ['OscillatorWaveShape2', 'Preserve'],
    ['OscillatorOct2', 'Preserve'],
    ['OscillatorSemi2', 'Preserve'],
    ['OscillatorDetune2', 'Consistency'],
    ['AttackTime', 'Type', 'Dynamics'],
    ['DecayTime', 'Dynamics'],
    ['SustainLevel', 'Dynamics'],
    ['SustainTime', 'Dynamics'],
    ['ReleaseTime', 'Dynamics'],
    ['AttackTime2', 'Type', 'Dynamics'],
    ['DecayTime2', 'Dynamics'],
    ['SustainLevel2', 'Dynamics'],
    ['SustainTime2', 'Dynamics'],
    ['ReleaseTime2', 'Dynamics'],
    ['VibratoSpeed', 'Consistency'],
    ['VibratoAmount', 'Consistency'],
    ['KeyboardUnison', 'Preserve'],
    ['KeyboardDetune', 'Consistency']
]

descriptors = [
    'Consistency',
    'Brightness',
    'Evolution',
    'Dynamics'
]

# We now need to figure out the combinations:
combinations = [
    [0, 0, 0], 
    [0, 0, 1], 
    [0, 0, 2], 
    [0, 1, 0], 
    [0, 1, 1], 
    [0, 1, 2], 
    [0, 2, 0], 
    [0, 2, 1], 
    [0, 2, 2], 
    [1, 0, 0], 
    [1, 0, 1], 
    [1, 0, 2], 
    [1, 1, 0], 
    [1, 1, 1], 
    [1, 1, 2], 
    [1, 2, 0], 
    [1, 2, 1], 
    [1, 2, 2], 
    [2, 0, 0], 
    [2, 0, 1], 
    [2, 0, 2], 
    [2, 1, 0], 
    [2, 1, 1], 
    [2, 1, 2], 
    [2, 2, 0], 
    [2, 2, 1], 
    [2, 2, 2]
]

# AUGMENTATION DICTIONARY:
augmentation_holder = {}
augmentation_holder['1'] = []
augmentation_holder['2'] = []
augmentation_holder['3'] = []
augmentation_holder['4'] = []
augmentation_holder['5'] = []
augmentation_holder['6'] = []
augmentation_holder['7'] = []
augmentation_holder['8'] = []
augmentation_holder['9'] = []
augmentation_holder['10'] = []
augmentation_holder['11'] = []
augmentation_holder['12'] = []
augmentation_holder['13'] = []
augmentation_holder['14'] = []
augmentation_holder['15'] = []
augmentation_holder['16'] = []
augmentation_holder['17'] = []
augmentation_holder['18'] = []
augmentation_holder['19'] = []
augmentation_holder['20'] = []
augmentation_holder['21'] = []
augmentation_holder['22'] = []
augmentation_holder['23'] = []
augmentation_holder['24'] = []
augmentation_holder['25'] = []
augmentation_holder['26'] = []
augmentation_holder['27'] = []

def augment_value(value, rule, operator):

    if (rule == "Preserve"):
        return value
        
    if (operator == 0):
        return value - 1
    elif (operator == 1):
        return value + 0
    elif (operator == 2):
        return value + 2
    
    return 69

def main():
    print('MAIN')

    
    # Read the csv:
    df_path = os.path.join('..', 'TrainingData', 'Datasets', 'Mar-16-2022.csv')
    df = pd.read_csv(df_path)
    df.head() 
    row = df.iloc[0]
    row_index = 0
    
    for x, combination in enumerate(combinations):
        print('-----------------------', combination, '------------------------')
        print('--------- Holder var: ', x + 1, '----------')
        for i in range(0, len(values), 3):
            a, b, c = values[i:i+3]
            print(a[0], ': ', row[str(a[0])], ' | ', combinations[x], end=" | ")
            print(b[0], ': ', row[str(b[0])], ' | ', combinations[x], end=" | ")
            print(c[0], ': ', row[str(c[0])], ' | ', combinations[x], end=" | ")
            print()

            # Implement rules:
            print(augment_value(value=row[str(a[0])], rule=a[1], operator=combination[0]))
            print(augment_value(value=row[str(b[0])], rule=b[1], operator=combination[1]))
            print(augment_value(value=row[str(c[0])], rule=c[1], operator=combination[2]))


            # Retrieve chunk values:
            value_01 = augment_value(value=row[str(a[0])], rule=a[1], operator=combination[0])
            value_02 = augment_value(value=row[str(b[0])], rule=b[1], operator=combination[1])
            value_03 = augment_value(value=row[str(c[0])], rule=c[1], operator=combination[2])

            # # Add to augment holder:
            augmentation_holder[str(x + 1)].append(value_01)
            augmentation_holder[str(x + 1)].append(value_02)
            augmentation_holder[str(x + 1)].append(value_03)

            print()
            print('---')
    
    print(augmentation_holder)


main()