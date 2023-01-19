"""
write a Python script to find and print the 10th word that has 
exactly 25 characters (not counting new line character '\n')
in /usr/share/dict/words
"""
word_lst = []

with open('/usr/share/dict/words', 'r') as f:
    for word in f:
        if len(word.strip('\n')) == 25:
            for i in range(10):        
                word_lst.append(word.strip('\n'))

    print(word_lst[9])



