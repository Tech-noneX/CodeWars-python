'''
Description:
You ask a small girl,"How old are you?" She always says, "x years old", 
where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, 
the test input may be "1 year old" or "5 years old". 
The first character in the string is always a number.
'''
#==========================automatically generated test data====================

import random

test_data = []
for loop in range(10):  # 10 test cases
    
    for loop in range(10):
        n = random.randint(0, 9)
     # saving data in format i need for testing   
    test_data.append((f"{n} years old", n))

#print(test_data)# this for me to see if list is ok for test

#------------------------------------------------------------------------------#

def get_age(age):
    age1 = []
    for char in age:
        age1.append(char)
    return int(age1[0])


def test_get_age():
    for feed,expected in test_data:
        assert get_age(age=feed) == expected