'''
Task:
Imagine you have a collection of blocks and want to know if you can arrange them into a perfect square—meaning, 
the total number of blocks forms a square shape (like 1x1, 2x2, 3x3, etc.).

Write a function that takes an integer and returns True if it is a perfect square, or False otherwise.

A perfect square is any whole number that can be written as another whole number multiplied by itself.

Examples:

Input: 9 → Output: True (since 3 x 3 = 9)

Input: 0 → Output: True (since 0 x 0 = 0)

Input: 7 → Output: False

Input: 16 → Output: True (since 4 x 4 = 16)

Input: 18 → Output: False

Input: -4 → Output: False


'''


#============================ test data generator ==============================
import random

 # list of numbers to be tested
numbers = []
 # list of pairs ready for test
test_data = []
 # number generator
for loop in range(100):
    number = random.randint(-50,50)
    numbers.append(number)
 # pair maker for test
for num in numbers:
    if num < 0 :
        test_data.append((num,False))
    elif (num ** 0.5).is_integer():
        test_data.append((num,True))
    else:
        test_data.append((num,False))
 # this 2 prints are for me to see the data
 # as data are random i want to see what data was used for test       
print(numbers)
print(test_data)


#--------------------------- tested function -----------------------------------


def is_square(n): 
    if n < 0 :
        return False
    if (n ** 0.5).is_integer():
        return True
    else:
        return False


#========================= Test ================================================
import pytest


@pytest.mark.parametrize("feed, expected", test_data)
def test_is_square(feed, expected):
    assert is_square(feed) == expected