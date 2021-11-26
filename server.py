from flask import Flask
from preset_extract import PresetManager
import numpy as np
import json

app = Flask(__name__)

categories = np.array([
    'Bass'
])

preset_manager = PresetManager(categories)

@app.route("/api/adv-files")
def get_adv():

    preset_paths = preset_manager.getPresetPaths()

    name =  []

    for preset in preset_paths:
        name.append(preset.name)

    return { 'presetNames': name}

@app.route("/api/get-json")
def get_json():
    json_array = preset_manager.get_json_array(0)
    return { 'presets': json_array}

@app.route('/api/get-presets')
def get_presets():
    preset_manager.get_presets_via_json()
    presets = preset_manager.presets

    preset_list = []

    for preset in presets:
        preset_list.append(preset.name)

    presets = { 'presets': preset_list}
    
    return presets


if __name__ == "__main__":
    app.run()