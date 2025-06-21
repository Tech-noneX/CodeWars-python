import random
'''
Description:
Create a function that takes 2 integers in form of a string as an input, 
and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
Notes:

If either input is an empty string, consider it as zero.

Inputs and the expected output will never exceed the
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
