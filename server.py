from flask import Flask, request, jsonify
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

@app.route('/api/get-presets') # For library view.
def get_presets():
    presets = preset_manager.get_preset_data()
    json = []

    for preset in presets:
        json.append(preset.format_to_json())
    
    
    return { 'presets': json }

@app.route('/api/find-new-data') # For train view.
def find_new_data():
    new_presets = preset_manager.get_new_data_v2()
    json = preset_manager.get_json_tree(new_presets)
    return json



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

@app.route('/api/newdata', methods=['POST'])
def new_data():
    input_json = request.get_json(force=True)
    
    # We need to create a function to store the new json data:



    return { 'hello': 'hello'}


if __name__ == "__main__":
    app.run()