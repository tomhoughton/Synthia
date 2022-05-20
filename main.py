import numpy as np
from preset_extract import Preset, PresetManager
from preset_extractV2 import PresetManager_V2, PresetV2
from preset_extractV3 import PresetManager_V3
from SynthiaStats import SynthiaStats
import xmltodict
from SynthiaV2 import Synthia

synthia = Synthia(df=None)

predicted_values = synthia.predict(model=None)
print(predicted_values)

data = synthia.export_preset(synthia_output=predicted_values)
