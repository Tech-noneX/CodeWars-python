import random
import string
'''
Description:
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
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