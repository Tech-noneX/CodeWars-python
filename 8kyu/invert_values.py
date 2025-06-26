'''
Task:
Write a function that takes a list of integers and returns a new list where each number is replaced by its opposite.
In other words, positive numbers become negative, and negative numbers become positive.

Examples:

[1, 2, 3, 4, 5] → [-1, -2, -3, -4, -5]

[1, -2, 3, -4, 5] → [-1, 2, -3, 4, -5]

[] → []

Note:
Don’t change the original list—return a new one.
'''

test_data = [
    ([1,2,3,4,5],[-1,-2,-3,-4,-5]),
    ([1,-2,3,-4,5], [-1,2,-3,4,-5]),
    ([], [])
    ]


def invert(lst):
    numbers = []
    for n in lst:
        n = n*-1
        numbers.append(n)
    return numbers

#--------------test----------------

def test_invert():
    for expected, numbers in test_data:
        assert invert(lst=numbers) == expected