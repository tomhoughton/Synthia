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
    data = preset_manager.get_preset_data()
    json = preset_manager.format_preset_data_for_api(data)
    
    return { 'presets': json }

@app.route('/api/stats')
def get_stats():
    # Firstly we need to get the total amount of presets
    preset_manager.get_presets_via_json()
    presets = preset_manager.presets
    preset_list = []

    for preset in presets:
        preset_list.append(preset.name)

    data = [
        { 'title': 'total presets', 'amount': len(preset_list), 'target': 1000},
        { 'title': 'Dynamic Low', 'amount': len(preset_list), 'target': 500},
        { 'title': 'Dynamic Mid', 'amount': len(preset_list), 'target': 300},
        { 'title': 'Dynamic High', 'amount': len(preset_list), 'target': 150},
        { 'title': 'Evolution Low', 'amount': len(preset_list), 'target': 300},
        { 'title': 'Evolution Mid', 'amount': len(preset_list), 'target': 345},
        { 'title': 'Evolution High', 'amount': len(preset_list), 'target': 234},
        { 'title': 'Consistency Low', 'amount': len(preset_list), 'target': 145},
        { 'title': 'Consistency Mid', 'amount': len(preset_list), 'target': 500},
        { 'title': 'Consistency High', 'amount': len(preset_list), 'target': 134},
        { 'title': 'Brightness Low', 'amount': len(preset_list), 'target': 169},
        { 'title': 'Brightness Mid', 'amount': len(preset_list), 'target': 221},
        { 'title': 'Brightness High', 'amount': len(preset_list), 'target': 121},
    ]

    return json.dumps(data)


if __name__ == "__main__":
    app.run()