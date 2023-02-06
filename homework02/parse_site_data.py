#!/usr/bin/env python3

import json
import math

ROBOT_LOC = {'latitude': 16.0, 'longitude': 82.0}
MAX_SPEED = 10
MARS_RADIUS = 3389.5    # km
STOP_TIME = {'stony': 1, 'iron': 2, 'stony-iron': 3}

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """
    Given latitude and longitude values of two points, the function `calc_gdc` calculates distance
    between points using the great-circle distance algorithm.

    Args:
        `latitude_1` (float): Value of first latitude point
        `longitude_1` (float): Value of first longitude point
        `latitude_2` (float): Value of second latitude point
        `longitude_2` (float): Value of second longitude point

    Returns:
        Distance calculation between two points (float), which is the result of multiplication between `MARS_RADIUS` and `d_sigma`
    """
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( MARS_RADIUS * d_sigma )

def calc_times(a_list_of_dicts: dict, a_key_string: str, index: int) -> tuple:
    """
    Iterates through a list of dictionaries, pulling out values associated with a given key at a given index.
    `calc_gcd()` function is then called to compute distance.
    Returns travel time and sampling time as a tuple.

    Args:
        `a_list_of_dicts` (dict): A list of dictionaries, each dict should have the same set of keys
        `a_key_string` (str): A key that appears in each dictionary associated with the desired value
        `index` (int): Index value of the list of sites associated with each dictionary containing the site's information

    Returns:
        A tuple containing `travel_time` and `sample_time`
        `travel_time` (float): Travel time from initial point to current point
        `sample_time` (int): Time taken to sample meteorite
    """
    if index == 0:
        # use robot's initial position and current position to calculate distance
        distance = calc_gcd(ROBOT_LOC['latitude'], ROBOT_LOC['longitude'], a_list_of_dicts[a_key_string][index]['latitude'], a_list_of_dicts[a_key_string][index]['longitude'])
        travel_time = round(distance/MAX_SPEED, 2)
        sample_time = STOP_TIME[a_list_of_dicts[a_key_string][index]['composition']]
    else:
        # use robot's previous location and current location to calculate distance
        distance = calc_gcd(a_list_of_dicts[a_key_string][index-1]['latitude'], a_list_of_dicts[a_key_string][index-1]['longitude'], a_list_of_dicts[a_key_string][index]['latitude'], a_list_of_dicts[a_key_string][index]['longitude'])
        travel_time = round(distance/MAX_SPEED, 2)
        sample_time = STOP_TIME[a_list_of_dicts[a_key_string][index]['composition']]

    return travel_time, sample_time


def main():
    # read json file
    with open('landing_sites.json', 'r') as f:
        landing_data = json.load(f)
    
    # initialize counter and total time
    i = 0
    total_time = 0

    # call function calc_times to get traveling time and sampling time, as well as calculate total time
    while i < len(landing_data['sites']):
        times = calc_times(landing_data, 'sites', i)
        i += 1
        total_time += (times[0] + times[1])
        print(f'leg = {i}, time to travel = {times[0]} hr, time to sample = {times[1]} hr')

    print('===============================')
    print(f'number of legs = {i}, total time to sample = {total_time} hr')

if __name__ == '__main__':
    main()
