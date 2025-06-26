'''
Task:
You'll receive two numbers representing the sides of a four-sided shape. Your job is to determine whether this shape is a square or a rectangle:

If both sides are the same length, calculate and return the area.

If the sides are different, return the perimeter instead.

Examples:

For sides 6 and 10, return 32 (since its a rectangle, the perimeter is 2 x (6 + 10) = 32).

For sides 3 and 3, return 9 (since its a square, the area is 3 x 3 = 9).

Note:
Treat the shape as a square if the two side lengths are equal; otherwise, its a rectangle.


'''


def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l * 2) + (w * 2)


#------------------test--------------------------


def test_are_or_perimeter():
    assert area_or_perimeter(10, 10) == 100
    assert area_or_perimeter(10, 20) == 60