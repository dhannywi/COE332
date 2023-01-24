"""
Write a Python script that use the names module to generate a list of five different full names. 
Define a function to determine the length of a given name (in number of characters, excluding spaces). 
Print to screen each name followed by the length of each name as an integer.
Course: COE 332
Name: Dhanny Indrakusuma
EID: dwi67
"""

import names

def name_length(n):
    return len(n.replace(" ", ""))

for i in range(5):
    f_name = names.get_full_name()
    print(f"{f_name}, {name_length(f_name)}")
