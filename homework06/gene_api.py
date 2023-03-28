#!/usr/bin/env python3

import json
from flask import Flask, request
import redis
import requests
import yaml

app = Flask(__name__)

# ---------------------------- Methods ---------------------------------
def get_redis_client():
    '''
    Function starts Redis server
    Returns:
        redis server connection
    '''
    return redis.Redis(host='redis-db', port=6379, db=0, decode_response=True)

 rd = get_redis_client()

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

@app.route('/data', methods=['POST', 'GET', 'DELETE'])
def hgnc_data() -> list:
    '''
    Function write/reads/delete data stored in redis database. Returns nested dictionaries. 
    Returns:
        result (list): List of nested dictionaries of the HGNC data  for "GET" method,
                       or status info (string) for "POST" and "DELETE" method.
    '''
    if request.method == 'GET':
        data = []
        try:
            for item in rd.keys():
                data.append(rd.hgetall(item))
        except Exception:
            return 'No data. Please use "POST" to load data.\n'
        return data

    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        for item in response.json()['response']['docs']:
            key = item['hgnc_id']
            rd.hset(key, mapping=item)
        return 'Data loaded\n'
    
    elif request.method == 'DELETE':
        rd.flushdb()
        return f'Data deleted, there are {len(rd.keys())} keys in the db\n'

    else:
        return 'The method you tried'

@app.route('/genes', methods=['GET'])
def get_hgnc_id() -> list:
    '''
    Function fetches data from db and return a list of all hgnc_id fields (set as keys in db).
    Returns:
        result (list): A list of hgnc_id
    '''
    if len(rd.keys()) == 0:
        return 'No data in db.\n'
    return rd.keys()

@app.route(/genes/<hgnc_id>) 
def get_gene_data() -> dict:
    '''
    Given a string, this function retrieve data, iterates through database 
    to retreive data from the requested hgnc_id.
    Returns a dictionary containing gene data for a given hgnc_id.
    Args:
        hgnc_id (str): A specific hgnc_id in the data set, requested by user.
    Returns:
        result (dict): Gene data for a specific hgnc_id from the database.
                       Returns an error message (str) in cases of invalid input or no data.
    '''
    if len(rd.keys()) == 0:
        return 'No data in db.\n'
    
    for item in rd.keys(): # get gene data using key, if data not in db, return error
        pass


if __name__ == '__main__':    
    config = get_config()
    if config.get('debug', True):
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run(host='0.0.0.0')

