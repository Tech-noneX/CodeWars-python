import random
import string
'''
Task:
Write a function that takes a string and returns a new string where every character 
(keeping upper and lower case as-is) appears twice in a row.

Examples:

"String" → "SSttrriinngg"

"Hello World" → "HHeelllloo WWoorrlldd"

"1234!_ " → "11223344!!__ "


'''
#=====================test data automatically generated==================

def double_char(s):
    string = ''
    for i in s:
        string += i * 2
    return string


#-------------------------test---------------------

def test_double_char():
    for loop in range(20):
        length = random.randint(1, 12)
        chars = string.ascii_letters + ' '
        feed = ''.join(random.choice(chars) for loop in range(length))
        expected = ''.join([c*2 for c in feed])
        assert double_char(feed) == expected