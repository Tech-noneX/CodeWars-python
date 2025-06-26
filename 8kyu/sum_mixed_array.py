import random

'''
Task:
You’re given a list that contains both numbers and strings representing numbers. Write a function that returns the sum of all these values as numbers.

Examples:

Input: [2, "5", 7, "3"] → Output: 17

Input: ["10", 4, "6"] → Output: 20

Input: [0, "0", 0] → Output: 0

Note:
Return the result as a numeric value, not a string.


'''


#========================test data automatically generated==============
test_data = []
for loop in range(5):
     # generates a list to feed test's  input and output 5x 
    length = random.randint(4, 10)  
    nums = []
    total = 0
    for loop in range(length):
         # generates data for the list randomly chosen int or str
        n = random.randint(0, 10)# int
        
        if random.choice([True, False]):
            nums.append(n)
        else:
            nums.append(str(n))# str
         # expected output is not include in random chosen data type so it is 
         # always integer 
        total += n
    test_data.append((nums, total))
#============================================================================
def sum_mix(arr):
    hok = []
    for i in arr:
        i = int(i)
        hok.append(i)
    return sum(hok)


#----------------------test-----------------------------


def test_sum_mix():
    for feed , expected in test_data:
        assert sum_mix(feed) == expected  