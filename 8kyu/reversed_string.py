'''
Task:
Write a function that takes a string and returns a new string with the characters in reverse order.

Examples:

Input: "python" → Output: "nohtyp"

Input: "racecar" → Output: "racecar"

Input: "hello" → Output: "olleh"


'''


#====================== data generator for test ================================
import random
import string

test_data = []

for loop in range(20):
    length = random.randint(3, 8)# length of each string
    
    for loop in range(length):
        chars = string.ascii_letters# letters
         # generating string of random length 
        feed = ''.join(random.choice(chars) for loop in range(length))
        expected = feed
     # save the data to test_data list ready to go    
    test_data.append((feed, expected[::-1]))
 # for me to se if data are ok
print(test_data) 


#-------------------------------------------------------------------------------


def solution(string):
    return string[::-1]


#======================= test ==================================================
import pytest

@pytest.mark.parametrize("feed, expected", test_data)
def test_solution(feed, expected):
    assert solution(feed) == expected