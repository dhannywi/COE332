#!/usr/bin/env python3

# import libraries
import datetime
import numpy as np
import pandas as pd
import requests


"""
Equation 1:
T = a0 * I90
T = # Turbidity in NTU Units (0 - 40)
a0 = # Calibration constant
I90 = # Ninety degree detector current
"""

"""
Equation 2:
Ts > T0(1-d)**b
Ts = 1.0 # Ts = Turbidity threshold for safe water (in NTU)
T0 = # T0 = Current turbidity
d = 0.02 # decay factor per hour, expressed as a decimal
b = # hours elapsed
"""

# https://www.educative.io/answers/how-to-compute-the-rolling-mean-of-a-time-series-in-python

def main():
    # fetch data
    data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    water_data = data.json()
    water_df = pd.DataFrame(water_data['turbidity_data'])

    print(water_df)

'''
sample output:

Average turbidity based on most recent five measurements = 1.1992 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 8.99 hours

Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
'''

if __name__ == '__main__':
    main()
