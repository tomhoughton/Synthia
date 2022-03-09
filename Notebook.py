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