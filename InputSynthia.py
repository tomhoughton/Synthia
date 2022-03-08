from preset_extractV3 import PresetManager_V3
import os

# This file is what will allow me to input data during development:

# Create a new manager object:
manager = PresetManager_V3()

# Get all the folders in new presets:
new_preset_folders = os.listdir('NewPresets')
preset_description_path = os.path.join('PresetDescriptions')

# Make a menu of sorts:
print('-----------------------')
print('| Synthia Input (Dev) |')
print('-----------------------')

# Print all of the presets with the index next to it:
for i, f in enumerate(new_preset_folders):
    print('[', i, ']', '-> ', f)
    
usr_input = input('Select the folder you would like to add to the dataset: ')

# Show the descriptions:
print('This is the folder: ', new_preset_folders[int(usr_input)])
print('These are the presets: ')
for i, f in enumerate(os.listdir(os.path.join('NewPresets', new_preset_folders[int(usr_input)]))):
    print('[', i, ']', '-> ', f)

# Store the folder to be used for preset generation:
folder_input = new_preset_folders[int(usr_input)]

# Get the description file:
# Print all of the description files:
print('Description Files: ')
for i, d in enumerate(os.listdir(preset_description_path)):
    print('[', i, ']', '-> ', d)
    
usr_input = input('Select the preset description file to use: ')
description_files = os.listdir(preset_description_path)
description_file = description_files[int(usr_input)]

print('-------------------------')
print('Folder of presets: ', folder_input)
print('Description File: ', description_file)


# Get the new data into json:
new_data = manager.get_new_data(folder=folder_input)

# Save the data:
manager.save_training_data(presets=new_data)

# Convert the data to a pandas dataframe:
manager.to_pandas_v2(description_file=description_file)

print('Conversion is complete')