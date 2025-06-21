from random import randint
'''
Description:
Code as fast as you can! You need to double the integer and return it.
'''


def double_integer(i):
    return i*2


#--------------------------test--------------------------


def test_double_integer():
    for loop in range(50):
        feed = randint(-1000,1000)
        expected = feed * 2
        assert double_integer(feed) == expected