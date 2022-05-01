import numpy as np
from preset_extract import Preset, PresetManager
from preset_extractV2 import PresetManager_V2, PresetV2
from preset_extractV3 import PresetManager_V3
from SynthiaStats import SynthiaStats

manager = PresetManager_V3()

# new_data = manager.get_new_data(folder='21stFeb')

# print(new_data)

# manager.save_training_data(presets=new_data)

# manager.to_pandas_v2(description_file='9thMarch.json')

import os
import pandas as pd
from SynthiaDataAugmentV2 import Augmentor
df_path = os.path.join('TrainingData', 'Datasets')
df = pd.read_csv(os.path.join(df_path, 'Mar-16-2022.csv'))

augmentor = Augmentor(df)
augmentor.gen()

# S_Stats = SynthiaStats(data=df)
# S_Stats.type_count()
# combination_counts = S_Stats.get_combination_counts()
# S_Stats.display_dataframe()
# print(combination_counts)
# print('----- Min and Max Test -----')
# S_Stats.get_combination_min_max()




