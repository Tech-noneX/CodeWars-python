from random import randint
'''
Task:
Write a function that takes an integer as input and returns the value you get by multiplying it by two.

Example:

Input: 7 → Output: 14
'''


def double_integer(i):
    return i*2


#--------------------------test--------------------------


def test_double_integer():
    for loop in range(50):
        feed = randint(-1000,1000)
        expected = feed * 2
        assert double_integer(feed) == expected