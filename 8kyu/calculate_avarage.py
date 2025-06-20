import pytest
'''
Description:
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
'''


def find_average(numbers):
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)


#----------Pytest-test----------


def test_find_average():
    assert find_average([10, 20, 30]) == 20


def test_find_average():
    assert find_average([]) == 0


