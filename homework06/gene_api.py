#!/usr/bin/env python3

from flask import Flask, request
import requests
import yaml

app = Flask(__name__)
data = {}
MEAN_EARTH_RADIUS = 6371.0

# ---------------------------- Methods ---------------------------------

def get_data() -> dict:
    '''
    Function fetches JSON data from a URL and returns data as nested dictionaries. 
    Args:
        None
    Returns:
        data (dict): Nested dictionaries of the HGNC data.
    '''
    global data
    data.clear()
    response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    return response.json()

def get_config() -> dict:
    '''
    Function reads a configuration file and return the associated values, or return a default.
    Args:
        None
    Returns:
        result (dict): A dictionary containing configuration (default or custom).
    '''
    default_config = {"debug": True}
    try:
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        # print(f"Couldn't load the config file; details: {e}")
        return default_config

# ---------------------------- API routes ---------------------------------

@app.route('/', methods=['GET'])
def get_hgnc_data() -> dict:
    '''
    Function reads data stored in the `data` global variable. Returns nested dictionaries. 
    Args:
        None
    Returns:
        data (dict): Nested dictionaries of the OEM data.
    '''
    if len(data) == 0:
        return 'No data found. Please reload data.\n', 400
    return data


