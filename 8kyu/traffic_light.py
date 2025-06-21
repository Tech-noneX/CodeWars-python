'''
Description:
You're writing code to control your town's traffic lights. 
You need a function to handle each change from green, 
to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing 
the current state of the light and returns a string representing the state 
the light should change to.

For example, when the input is green, output should be yellow.
'''

test_data = {'green': 'yellow', 'yellow': 'red', 'red': 'green'}


def update_light(current):
    if current == 'green':
        return 'yellow'
    if current == 'yellow':
        return 'red'
    if current == 'red':
        return 'green'


#======================test===========================

def test_update_light():
    for feed, expected in test_data.items():
        assert update_light(feed) == expected