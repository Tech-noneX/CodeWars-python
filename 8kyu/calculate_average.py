import pytest
'''
Task:
Create a function that takes a list of numbers and returns their average.

If the list is empty, your function should return 0.
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


