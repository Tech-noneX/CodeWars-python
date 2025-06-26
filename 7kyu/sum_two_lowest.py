'''
Task:
Write a function that takes a list of at least four positive integers 
and returns the sum of the two smallest numbers in the list.

All inputs will be positive whole numbers (no decimals or zero).

The list will always contain at least four numbers.

Examples:

Input: [8, 21, 4, 15, 99] → Output: 12 (since 4 + 8 = 12)

Input: [100, 200, 1, 50, 7] → Output: 8 (since 1 + 7 = 8)

Input: [13, 22, 5, 45, 18, 30] → Output: 18 (since 5 + 13 = 18)


'''


#======================== test data generator ==================================
import random
 # list of lists (random length, random numbers)
random_lists = []
 # addition of 2 min numbers from each lists in numbers
sum_min = [] 
 # number of lists in the list
num_of_seq = 150
for loop in range(num_of_seq):
     # makes random length of lists
    list_length = random.randint(5,10)
    seq = []

    for loop in range(list_length):
         # makes random numbers in random lists and append them to list seq
        seq.append(random.randint(-20,500))
     # takes all lists cooked and append them to min one
    random_lists.append(seq) 

for seq in random_lists:
     # temporary sort numbers in list to make them ready for addition 2 min num
    sorted_seq = sorted(seq) 
     # Calculate the sum of the two smallest numbers in each list 
    min_pair_sum = sorted_seq[0] + sorted_seq[1]
     # result is sent to list sum_min
    sum_min.append(min_pair_sum)
 # Pair input/output for automated test data
test_data = [(feed,expected) for feed,expected in zip(random_lists,sum_min)]
 # for overview to see if is going good
print(seq)
print(random_lists)
print(sum_min)
print(test_data)


#-------------------------- Function -------------------------------------------


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


#================================ Test =========================================
import pytest

@pytest.mark.parametrize("feed, expected", test_data)
def test_sum_two_smallest(feed, expected):
    assert sum_two_smallest_numbers(feed) == expected