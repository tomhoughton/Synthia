from flask import Flask, request, jsonify
from preset_extract import PresetManager
from preset_extractV2 import PresetManager_V2
import numpy as np
import json

app = Flask(__name__)

categories = np.array([
    'Bass'
])

preset_manager = PresetManager(categories)
preset_managerV2 = PresetManager_V2()

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
    presets = preset_managerV2.get_preset_dataV2()

    return { 'presets': presets }

@app.route('/api/find-new-data') # For train view.
def find_new_data():
    new_presets = preset_managerV2.get_new_data_v3()
    return json.dumps(new_presets)



@app.route('/api/stats')
def get_stats():
   
    data = preset_managerV2.refresh_stats()
    descriptors = data['descriptorMatrix']
    descriptors_sum = np.sum(descriptors)

    consistency = [
        ((descriptors[0][0] / descriptors_sum) * 100),
        ((descriptors[0][1] / descriptors_sum) * 100),
        ((descriptors[0][2] / descriptors_sum) * 100),
    ]
    

    brightness = [
        ((descriptors[1][0] / descriptors_sum) * 100),
        ((descriptors[1][1] / descriptors_sum) * 100),
        ((descriptors[1][2] / descriptors_sum) * 100),
    ]

    
    dynamics = [
        ((descriptors[2][0] / descriptors_sum) * 100),
        ((descriptors[2][1] / descriptors_sum) * 100),
        ((descriptors[2][2] / descriptors_sum) * 100),
    ]

    
    evolution = [
        ((descriptors[3][0] / descriptors_sum) * 100),
        ((descriptors[3][1] / descriptors_sum) * 100),
        ((descriptors[3][2] / descriptors_sum) * 100),
    ]


    data = [
        { 'title': 'total presets', 'amount': 'totalPresets', 'target': 100},
        { 'title': 'Dynamic Low', 'amount': dynamics[0], 'target': 500},
        { 'title': 'Dynamic Mid', 'amount': dynamics[1], 'target': 300},
        { 'title': 'Dynamic High', 'amount': dynamics[2], 'target': 150},
        { 'title': 'Evolution Low', 'amount': evolution[0], 'target': 300},
        { 'title': 'Evolution Mid', 'amount': evolution[1], 'target': 345},
        { 'title': 'Evolution High', 'amount': evolution[2], 'target': 234},
        { 'title': 'Consistency Low', 'amount': consistency[0], 'target': 145},
        { 'title': 'Consistency Mid', 'amount': consistency[1], 'target': 500},
        { 'title': 'Consistency High', 'amount': consistency[2], 'target': 134},
        { 'title': 'Brightness Low', 'amount': brightness[0], 'target': 169},
        { 'title': 'Brightness Mid', 'amount': brightness[1], 'target': 221},
        { 'title': 'Brightness High', 'amount': brightness[2], 'target': 121},
    ]

    return json.dumps(data)

@app.route('/api/newdata', methods=['POST'])
def new_data():
    input_json = request.get_json(force=True)
    
    preset_manager.save_training_data(input_json['presets'])

    print('CLEAR')
    preset_manager.clear_NewPresets_folder(input_json['presets'])

    return { 'hello': 'hello'}


if __name__ == "__main__":
    app.run()



