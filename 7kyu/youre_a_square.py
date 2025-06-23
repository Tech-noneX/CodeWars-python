'''
Description:
A square of squares
You like building blocks. You especially like building blocks that are squares. 
And what you even like more, is to arrange them into a square of square building blocks!
However, sometimes, you can't arrange them into a square. 
Instead, you end up with an ordinary rectangle! Those blasted things! 
If you just had a way to know, whether you're currently working in vain… Wait! 
That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer 
that is the square of an integer; in other words, 
it is the product of some integer with itself.
The tests will always use some integral number, 
so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
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