'''
Create a function that returns the sum of the two lowest positive numbers 
given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], 
the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
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