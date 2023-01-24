"""
Write a Python script to find and print the five longest words in the words file from earlier in this guide. Ties go to the words that would appear first alphabetically.
Course: COE 332
Name: Dhanny Indrakusuma
EID: dwi67
"""

words = []

# read file
with open('words', 'r') as infile:
    words = infile.read().splitlines()

# sort from longest to shortest words
words.sort(key=len, reverse=True)
# top 5 longest, alphabetically
result = words[:5]

# print result
for i in result:
    print(i)
