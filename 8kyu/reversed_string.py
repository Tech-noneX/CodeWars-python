'''
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
'''


#====================== data generator for test ================================
import random
import string

test_data = []

for loop in range(20):
    length = random.randint(3, 8)# length of each string
    
    for loop in range(length):
        chars = string.ascii_letters# letters
         # generating string of random length 
        feed = ''.join(random.choice(chars) for loop in range(length))
        expected = feed
     # save the data to test_data list ready to go    
    test_data.append((feed, expected[::-1]))
 # for me to se if data are ok
print(test_data) 


#-------------------------------------------------------------------------------


def solution(string):
    return string[::-1]


#======================= test ==================================================


def test_solution():
    for feed,expected in test_data:
        assert solution(feed) == expected