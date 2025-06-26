'''
Task:
Write a function that takes a number (it could be positive, negative, or zero) and returns its opposite value.

Examples:

Input: 5 → Output: -5

Input: -12.5 → Output: 12.5

Input: 0 → Output: 0
'''


def opposite(number):
    if number == 0:
        return 0
    if number < 0:
        return (-number - (-number) -(number)) 
    if number > 0:
        return (number - number) - number 


#----------------------test--------------------------


def test_opposite():
    assert opposite(1) == -1
    assert opposite(-1) == 1
    assert opposite(0) == 0
    assert opposite(2.36) == -2.36
    assert opposite(-3.68) == 3.68