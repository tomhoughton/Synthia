from flask import Flask, request
import numpy as np
import json
from preset_extractV3 import PresetManager_V3

# Create the app:
app = Flask(__name__)

"""MIGHT NEED TO DELETE"""
categories = np.array(['Bass'])

# Create a new preset manager object:
PMV3 = PresetManager_V3()

@app.route('api/get-presets') # For Library View:
def get_presets():

    # Get the data:
    presets = PMV3.get_preset_dataV2()

    # Return the data:
    return { 'presets': presets }

@app.route('/api/find-new-data') # For Train View:
def find_new_data():

    # Get the data:
    new_presets = PMV3.get_new_data_V3()
    
    # Return the data:
    return json.dumps(new_presets)

@app.route('api/newdata', methods=['POST'])
def new_data():

    # Get the http req data:
    input_json = request.get_json(force=True)

    # Save the training data:
    PMV3.save_training_data(input_json['presets'])
    
    # Clear the new presets folder: 
    PMV3.clear_new_presets(input_json['presets'])

if __name__=="__main__":
    app.run()