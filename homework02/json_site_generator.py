#!/usr/bin/env python3

import json
import random

def generate_sites(lat1: float, lat2: float, long1: float, long2: float) -> dict:
    """
    Given upper and lower bounds of latitude and longtitude, this function randomly
    generates latitude, longitude, and compositions for the five meteorite landing sites.
    Returns a dictionary (in json format) containing the landing sites details.

    Args:
        `lat1` (float): A lower bound latitude value
        `lat2` (float): An upper bound latitude value
        `long1` (float): A lower bound longtitude value
        `long2` (float): An upper bound longtitude value

    Returns:
        `data` (dict): A dictionary with a single key,
                       with value of a list of dictionaries containing
                       information to meteorite landing sites details
    """
    composition_list = ["stony", "iron", "stony-iron"]

    data = {}
    data['sites'] = []
    for i in range(5):
        data['sites'].append( {"site_id": i+1,\
                               "latitude": random.uniform(lat1, lat2),\
                               "longtitude": random.uniform(long1, long2),\
                               "composition": random.choice(composition_list)} )
    return data

def main():
    """
    Initialize random site generator and write data into a json file
    """
    with open('landing_sites.json', 'w') as out:
        json.dump( generate_sites(16.0, 18.0, 82.0, 84.0), out, indent=2)

if __name__ == '__main__':
    main()
