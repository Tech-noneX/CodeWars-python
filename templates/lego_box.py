'''
import random
import string
import pytest
test_data =[]
for loop in range(5):  # 5 test cases
length = random.randint(4, 10)  # random length of each list
nums = []
total = 0
n = random.randint(0, 10)
        # Randomly decide: keep as int or convert to str
random.choice([True, False]):
nums.append(n)
        
nums.append(str(n))
total += n
test_data.append((nums, total))
test_data = []
for loop in range(10):  # 10 test cases
for loop in range(10):
n = random.randint(0, 9)
    
test_data.append((n , n))

chars = string.ascii_letters + ' '
feed = ''.join(random.choice(chars) for loop in range(length))
'''

'''
@pytest.mark.parametrize("feed, expected", test_data)
def test_reverse_string(feed, expected):
    assert reverse_string(feed) == expected
'''