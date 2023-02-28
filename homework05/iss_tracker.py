#!/usr/bin/env python3

from flask import Flask, request
from math import sqrt
import requests
import xmltodict

app = Flask(__name__)
data = {}

def get_data() -> dict:
    '''
    Function fetches XML data from a URL and returns XML data as nested dictionaries. 
    Args:
        None
    Returns:
        data (dict): Nested dictionaries of the OEM data.
    '''
    data.clear()
    response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text) # xmltodict.parse(response.content) works too
    return data

@app.route('/', methods=['GET'])
def get_oem_data() -> dict:
    '''
    Function reads data stored in the `data` global variable. Returns nested dictionaries. 
    Args:
        None
    Returns:
        data (dict): Nested dictionaries of the OEM data.
    '''
    return data

@app.route('/epochs', methods=['GET'])
def get_epochs() -> list:
    '''
    Function fetches data stored in `data` global variable and iterates through the nested dictionary using a set of keys.
    Returns a list of epochs present in the dataset.
    Args:
        none
    Returns:
        epochs (list): A list of all Epochs in the data set.
    '''
    epochs = []
    for i in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        epochs.append(i['EPOCH'])
    return epochs

# add: /epochs?limit=int&offset=int
# implement try/except

@app.route('/epochs/<epoch>', methods=['GET'])
def get_state_vectors(epoch: str) -> dict:
    '''
    Given a string, this function calls `get_oem_data()` function to retrieve data, 
    iterates through the nested dictionaries generated with a set of keys to retreive data for the requested epoch.  
    Returns a dictionary containing information for a given epoch.
    Args:
        epoch (str): A specific Epoch in the data set, requested by user.
    Returns:
        result (dict): State vectors for a specific Epoch from the data set. Returns a string if epoch requested does not exist.
    '''
    try:
        data['ndm']['oem']['body']['segment']['data']['stateVector']['EPOCH']
    except ValueError:
        return 'Invalid Request\n'

    for i in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        if i['EPOCH'] != epoch:
            continue
        elif i['EPOCH'] == epoch:
            return i
        else:
            return 'The epoch you requested is not in the data.\n', 400

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
    # idea: maybe check for error. Eg: get_state_vectors() != 400
    # or maybe this might work too? try: get_state_vectors()
    # Exception will return the error string
    '''
    try:
        get_state_vectors()
    except #type:
        return 'We are unable to calculate speed as the Epoch you requested is not in the data.\n', 400
    '''
    state_vector = get_state_vectors(epoch)
    x_dot = float(state_vector['X_DOT']["#text"])
    y_dot = float(state_vector['Y_DOT']["#text"])
    z_dot = float(state_vector['Z_DOT']["#text"])

    speed = sqrt( (x_dot**2) + (y_dot**2) + (z_dot**2) )
    return f'The instantaneous speed for Epoch: {epoch} is { round(speed, 4) } km/s.\n'
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
'''

@app.route('/help', methods=['GET'])
def help_info() -> str:
    '''
    Function returns help text (as a string) that briefly describes each route.
    Args:
        None
    Returns:
        help_str (str):  Help text that briefly describes each route
    '''
    help_str = '''
    Usage: ISS Tracker App

    A Flask application for querying and returning interesting information from the ISS data set.

    Route                           Method  What it should do
    /                               GET     Return entire data set
    /epochs                         GET     Return list of all Epochs in the data set
    /epochs?limit=int&offset=int    GET     Return modified list of Epochs given query parameters
    /epochs/<epoch>                 GET     Return state vectors for a specific Epoch from the data set
    /epochs/<epoch>/speed           GET     Return instantaneous speed for a specific Epoch in the data set
    /help                           GET     Return help text that briefly describes each route
    /delete-data                    DELETE  Delete all data from the dictionary object
    /post-data                      POST    Reload the dictionary object with data from the web

    You can find more information about the dataset used in the ISS Trajectory Data website:
    https://spotthestation.nasa.gov/trajectory_data.cfm

    Please refer to ISS Tracker App's repository for more information:
    https://github.com/dhannywi/COE332/tree/main/homework05\n'''
    
    return help_str

@app.route('/delete-data', methods=['DELETE'])
def delete_data() -> str:
    '''
    Function to clear data stored in the `data` global variable.
    Args:
        None
    Returns:
        result (str): String confirming deletion of data.
    '''
    global data
    data.clear()
    return 'All the data has been removed.\n'

@app.route('/post-data', methods=['POST'])
def post_data() -> dict:
    '''
    Function to populate (or re-populate) `data` global variable with the OEM data set.
    Args:
        None
    Returns:
        data (dict): Nested dictionaries of the OEM data.
    '''
    global data
    get_data()
    return data

if __name__ == '__main__':
    get_data()
    app.run(debug=True, host='0.0.0.0')
