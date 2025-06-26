import random
'''
Task:
Write a function that accepts two values, each representing an integer in string format. 
Your function should return their sum, also as a string.

If either input is an empty string, treat it as zero.

Both positive and negative numbers are possible.

Examples:

Input: "7", "12" → Output: "19"

Input: "-8", "5" → Output: "-3"

Input: "", "4" → Output: "4"

Input: "", "" → Output: "0"

Input: "100", "" → Output: "100"
'''
#====================test data generator========================


test_data = []
for loop in range(5):  # 5 test cases
    
    for loop in range(2):
         # makes list of string numbers for both 'a' and 'b' input
        a = random.randint(0, 10)
        b = random.randint(10, 20)
         # append numbers in pairs good for testing
        test_data.append((str(a),str(b)))    
        

#--------------------------------------------------------------------------


def sum_str(a, b):
    if a == '':
        a = 0
    if b == '':
        b = 0
    sum = int(a) + int(b)
    return str(sum)


#-------------------test--------------------------------------------------


def test_sum_str():
    for feed_a,feed_b in test_data:
        expected = str(int(a) + int(b))
        assert sum_str(a=feed_a,b=feed_b) == expected


def test_sum_empty_str():
    feed_a,feed_b = '',''
    assert sum_str(a=feed_a,b=feed_b) == '0'
