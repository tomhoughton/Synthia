import numpy as np
from preset_extract import PresetManager

# Important variables:
categories = np.array([
    'Bass',
    'Brass',
    'Effects',
    'Guitar & Plucked',
    'Piano & Keys',
    'Synth Lead',
    'Synth Misc',
    'Synth Pad',
    'Synth Percussion',
    'Voices'
])

# Create a preset manager instance.
preset_manager = PresetManager(categories)

preset_paths = preset_manager.getPresetPaths()

for i in preset_paths:
    print(i.name)

print("Shape", preset_paths.shape)
