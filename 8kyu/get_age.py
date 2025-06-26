'''
Task:
A young girl always responds to the question “How old are you?” 
with a phrase like “3 years old” or “7 years old”, where the number at the start (between 0 and 9) is her age.

Write a function that takes this response as a string and returns her age as an integer.

Note:
The input will always start with a single-digit number, and the format will be consistent.


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

#-----------------------------------test----------------------------------------


def test_get_age():
    for feed,expected in test_data:
        assert get_age(age=feed) == expected