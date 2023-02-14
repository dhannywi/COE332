#!/usr/bin/env python3

# import module to be tested
from analyze_water import turbidity, min_return_time
import pytest

def test_turbidity():
    '''
    Tests `turbidity()` function from `analyze_water` module for correct calculation result and correct output type.
    '''
    assert turbidity({'calibration_constant': 0.97, 'detector_current': 1.15}) == 1.1155
    assert isinstance( turbidity({'calibration_constant': 1.027, 'detector_current': 1.16}), float) == True

def test_min_return_time():
    '''
    Tests `min_return_time()` function from `analyze_water` module for correct calculation results and correct output types, for cases when average turbidity is above or below normal threshold.
    '''
    assert min_return_time( 0.815 ) == 0
    assert min_return_time( 1.1601 ) == 7.35
    assert isinstance( min_return_time( 0.815 ), int ) == True
    assert isinstance( min_return_time( 1.1601 ), float ) == True
