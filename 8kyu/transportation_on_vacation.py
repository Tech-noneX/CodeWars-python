'''
Task:
You’re planning a trip and want to know how much it will cost to rent a car. The daily rental price is $40.

If you rent the car for 7 days or more, you receive a $50 discount on the total.

If you rent for at least 3 days (but less than 7), you get $20 off the total price.

Rentals shorter than 3 days get no discount.

Write a function that takes the number of days as input and returns the total rental cost.

Examples:

Input: 8 → Output: 270 (8 x $40 = $320, minus $50 discount)

Input: 5 → Output: 180 (5 x $40 = $200, minus $20 discount)

Input: 2 → Output: 80 (2 x $40 = $80, no discount)


'''

#==========================automatically generated test data====================


import random

test_data = []
for loop in range(10):  # 10 test cases
    
    for loop in range(10):
        n = random.randint(0, 21)
         # calculating output for test
        if n >= 7:
            price = (n * 40) - 50
        elif n >= 3 :
            price = (n * 40) - 20
        else:
            price = n * 40
        
     # saving data in format i need for testing   
    test_data.append((n, price))
print(test_data)

#-------------------------------------------------------------------------------


def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        return cost - 50
    elif d >= 3:
        return cost - 20
    else:
        return cost


#----------------------test-----------------------------------------------------


def test_rental_cost():
    for feed,price in test_data:
        expected = price
        assert rental_car_cost(feed) == expected