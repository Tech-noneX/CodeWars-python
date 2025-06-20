'''
Description:
Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
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