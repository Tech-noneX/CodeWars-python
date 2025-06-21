'''
Description:
Create a function that takes an integer as an argument 
and returns "Even" for even numbers or "Odd" for odd numbers.
'''
test_data ={2: 'even', 10: 'even', -1: 'odd', -10: 'even', 23: 'odd',
55: 'odd', 101: 'odd', 266: 'even'}




def even_or_odd(number):
    if number%2 == 0:
        return 'even'
    else:
        return 'odd'


#----------------test-------------------

def test_even_or_odd():
    for number, expected in test_data.items():
        assert even_or_odd(number=number) == expected 















