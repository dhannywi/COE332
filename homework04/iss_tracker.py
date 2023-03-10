#!/usr/bin/env python3

from flask import Flask
from math import sqrt
import requests
import xmltodict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_oem_data() -> dict:
    '''
    Function fetches XML data from a URL and returns XML data as nested dictionaries. 
    Args:
        None
    Returns:
        result (dict): Nested dictionaries of the OEM data.
    '''
    response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    return xmltodict.parse(response.text) # xmltodict.parse(response.content) works too

@app.route('/epochs', methods=['GET'])
def get_epochs() -> list:
    '''
    Function calls `get_oem_data()` to fetch data and iterates through the nested dictionary using a set of keys.
    Returns a list of epochs present in the dataset.
    Args:
        none
    Returns:
        epochs (list): A list of all Epochs in the data set.
    '''
    epochs = []
    for i in get_oem_data()['ndm']['oem']['body']['segment']['data']['stateVector']:
        epochs.append(i['EPOCH'])
    return epochs

@app.route('/epochs/<epoch>', methods=['GET'])
def get_state_vectors(epoch: str) -> dict:
    '''
    Given a string, this function calls `get_oem_data()` function to retrieve data, 
    iterates through the nested dictionaries generated with a set of keys to retreive data for the requested epoch.  
    Returns a dictionary containing information for a given epoch.
    Args:
        epoch (str): A specific Epoch in the data set, requested by user.
    Returns:
        result(dict): State vectors for a specific Epoch from the data set. Returns a string if epoch requested does not exist.
    '''
    for i in get_oem_data()['ndm']['oem']['body']['segment']['data']['stateVector']:
        if i['EPOCH'] != epoch:
            continue
        elif i['EPOCH'] == epoch:
            return i
        else:
            return 'The epoch you requested is not in the data.\n'

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def calculate_speed(epoch: str) -> str:
    '''
    Given a string, this function calls the `get_state_vectors()` function to retrieve the state vector (dict) for a given epoch.
    Iterates through the dictionary, pulling out values associated with a given key.
    Returns instantaneous speed for a specific epoch in the data set.
    Args:
        epoch (str): A specific Epoch in the data set, requested by user.
    Returns:
        result (str): Instantaneous speed (float) for a specific Epoch in the data set, expressed as a string output.
                      Speed is rounded to the nearest 4 decimal points.
    '''
    if type(get_state_vectors(epoch)) == dict:
        data = get_state_vectors(epoch)
        x_dot = float(data['X_DOT']["#text"])
        y_dot = float(data['Y_DOT']["#text"])
        z_dot = float(data['Z_DOT']["#text"])

        speed = sqrt( (x_dot**2) + (y_dot**2) + (z_dot**2) )
        return f'The instantaneous speed for the epoch you requested is { round(speed, 4) } km/s.\n'
    else:
        return 'We are unable to calculate speed as the epoch you requested is not in the data.\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
