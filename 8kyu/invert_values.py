'''
Description:
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
You can assume that all values are integers. Do not mutate the input array.
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