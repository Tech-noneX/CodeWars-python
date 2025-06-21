import random
import string

test_data = []
for loop in range(5):  # 5 test cases
    length = random.randint(4, 10)  # random length of each list
    nums = []
    total = 0
    for loop in range(length):
        n = random.randint(0, 10)
        # Randomly decide: keep as int or convert to str
        if random.choice([True, False]):
            nums.append(n)
        else:
            nums.append(str(n))
        total += n
    test_data.append((nums, total))
test_data = []
for loop in range(10):  # 10 test cases
    
    for loop in range(10):
        n = random.randint(0, 9)
     # saving data in format i need for testing   
    test_data.append((n , n))

chars = string.ascii_letters + ' '
feed = ''.join(random.choice(chars) for loop in range(length))
import pytest

'''
@pytest.mark.parametrize("feed, expected", test_data)
def test_reverse_string(feed, expected):
    assert reverse_string(feed) == expected
'''