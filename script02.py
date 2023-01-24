"""
Write a Python script that uses the names module to print out
five names that are exactly eight characters each
(nine characters if you include the space).
Course: COE 332
Name: Dhanny Indrakusuma
EID: dwi67
"""

import names

i = 0
while i < 5:
    new_name = names.get_first_name()
    if len(new_name) == 8:
        print(new_name)
    else:
        continue
    i += 1
