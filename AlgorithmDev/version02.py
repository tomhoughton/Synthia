import pandas as pd
import os

# Since the dataset does not concat onto the original one, we can do this in any order.
# A new rule needs to be implemented to consider features where 0.5 is regarded as the '0' point.

# IMPORTANT VARIABLES:
meta = [
    'Name',
    'Type',
    'Consistent',
    'Bright',
    'Evolves',
    'Dynamic',
    'Consistency',
    'Brightness',
    'Evolution',
    'Dynamics',
    'KeyboardUnisonToggle'

]

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

def apply_meta_data(row, combination):
    print('####### apply_meta_data #########')
    
    rtn = []

    for m in meta:
        if m=='Name':
            rtn.append(row[m] + "_" + str(combination))
        else:
            rtn.append(row[m])

    return rtn

def add_to_dictionary(new_rows):

    pd_dictionary = {}

    # Descriptors 01:
    pd_dictionary['Name'] = []
    pd_dictionary['Type'] = []
    pd_dictionary['Consistent'] = []
    pd_dictionary['Bright'] = []
    pd_dictionary['Evolves'] = []
    pd_dictionary['Dynamic'] = []
    pd_dictionary['Consistency'] = []
    pd_dictionary['Brightness'] = []
    pd_dictionary['Evolution'] = []
    pd_dictionary['Dynamics'] = []

    # Oscillator 01:
    pd_dictionary['OscillatorWaveShape'] = []
    pd_dictionary['OscillatorOct'] = []
    pd_dictionary['OscillatorSemi'] = []
    pd_dictionary['OscillatorDetune'] = []

    # Filter and LFO:
    pd_dictionary['FilterCutoffFrequency'] = []
    pd_dictionary['FilterLFOCutoffMod'] = []
    pd_dictionary['FilterEnvCutoffMod'] = []
    pd_dictionary['LFOSpeed'] = []
    pd_dictionary['LFOFadeIn'] = []

    # Oscillator 02:
    pd_dictionary['OscillatorWaveShape2'] = []
    pd_dictionary['OscillatorOct2'] = []
    pd_dictionary['OscillatorSemi2'] = []
    pd_dictionary['OscillatorDetune2'] = []

    # Envelope 01:
    pd_dictionary['AttackTime'] = []
    pd_dictionary['DecayTime'] = []
    pd_dictionary['SustainLevel'] = []
    pd_dictionary['SustainTime'] = []
    pd_dictionary['ReleaseTime'] = []

    # Envelope 02:
    pd_dictionary['AttackTime2'] = []
    pd_dictionary['DecayTime2'] = []
    pd_dictionary['SustainLevel2'] = []
    pd_dictionary['SustainTime2'] = []
    pd_dictionary['ReleaseTime2'] = []

    # Globals:
    pd_dictionary['VibratoSpeed'] = []
    pd_dictionary['VibratoAmount'] = []
    pd_dictionary['KeyboardUnison'] = []
    pd_dictionary['KeyboardUnisonToggle'] = []
    pd_dictionary['KeyboardDetune'] = []

    for row in new_rows:
        
        # Meta:
        for index, m in enumerate(meta):
            pd_dictionary[m].append(row[index])


        # Values:
        row_slice = row[len(meta):]

        for index, v in enumerate(values):
            pd_dictionary[v[0]].append(row_slice[index])

        print(pd_dictionary)

    data_frame = pd.DataFrame(pd_dictionary)
    data_frame.to_csv('augmented')

    # Values:


    

def main():
    print('MAIN')

    # Get the dataset:
    df_path = os.path.join('Mar-16-2022.csv')
    df = pd.read_csv(df_path)

    # Holds each augmented row:
    new_rows = []

    # Loop in range to loop through all rows:
    for row_index in range(0, (len(df.to_numpy()))):
        # Get the row:
        row = df.iloc[row_index]
        print('---- New Original Row ---', ' Index: ', row_index)
        print(row)
        # Now we need to loop through each combination:
        for x, combination in enumerate(combinations):
            # Debug print combination:
            print('-------------------------------', combination, '--------------------------')
            print('NewRow')

            holder = []

            # We need to apply the meta/descriptor data to the list:
            holder = apply_meta_data(row=row, combination=combination) # Next we need to add this to the list and make sure we're not loosing any data.

            # Loop through the augmentable values in grooups of three:
            for i in range(0, len(values), 3):
                v_1, v_2, v_3 = values[i:i+3]

                # Retrive augmented values:
                value_01 = augment_value(value=row[str(v_1[0])], rule=v_1[1], operator=combination[0])
                value_02 = augment_value(value=row[str(v_2[0])], rule=v_2[1], operator=combination[1])
                value_03 = augment_value(value=row[str(v_3[0])], rule=v_3[1], operator=combination[2])

                holder.append(value_01)
                holder.append(value_02)
                holder.append(value_03)



            print(holder)
            new_rows.append(holder)
        
        print('--------- INITIATE NEW ROW AUGMENTATION -------------------')
        print(new_rows)
    
    print('----- Now Its Time to try and place this into a dictionary -----')
    add_to_dictionary(new_rows=new_rows)
    
    
main()