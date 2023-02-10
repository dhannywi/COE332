#!/usr/bin/env python3

# import libraries
import requests
from math import log

TS = 1.0 # Turbidity threshold for safe water (in NTU)
D = 0.02 # decay factor per hour, expressed as a decimal


def turbidity(data: list) -> float:
    """
    Iterates through a list of dictionaries, calculates water turbidity based on readings taken by a nephelometer.
    Returns the product of calibration constant and ninety degree detector current.
    
    Args:
        data (list): A list of dictionaries, each dict should have the same set of keys.

    Returns:
        result (float): Water turbidity in NTU Units.
    """
    return data['calibration_constant'] * data['detector_current']


def min_return_time(T0: float) -> float:
    """
    Given the value of current water turbidity, function calculates minimum time to return below a safe threshold.

    Args: 
        T0 (float): Current turbidity (average value of 5 most recent readings).
    
    Returns:
        b (float): Minimum time to return below a safe threshold. Time is 0 if water is already below a safe treshold, otherwise it returns time needed, rounded to 2 decimal points.
    """
    b = round( (log(TS/T0) / log(1-D)), 2)
    if b < 0:
        b = 0
        return b
    else:
        return b


def main():
    # fetch data
    data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    water_data = data.json()
    # get data for 5 most recent readings
    data_last_5 = [ i for i in water_data['turbidity_data'][-5:] ]
    
    # calculate total turbidity and average turbidity of 5 most recent readings
    total_turbidity = 0
    for e in data_last_5:
        total_turbidity += turbidity(e)
    
    avg_turbidity = round( (total_turbidity / 5), 4)
    print(f'Average turbidity based on most recent five measurements = {avg_turbidity} NTU')

    # print whether boil water notice is issued and calculates minimum time to return below a safe threshold if necessary
    if avg_turbidity < TS:
        print(f'Info: Turbidity is below threshold for safe use')
    else:
        print(f'Warning: Turbidity is above threshold for safe use')
    print(f'Minimum time required to return below a safe threshold = {min_return_time(avg_turbidity)} hours')


if __name__ == '__main__':
    main()
