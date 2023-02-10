#!/usr/bin/env python3

# import module to be tested
from analyze_water import turbidity, min_return_time
import pytest

def test_turbidity():
    assert turbidity( info_to_pass_to_func1 ) == expected_value

def test_min_return_time():
    assert min_return_time( info_to_pass_to_func2 ) == expected_value
