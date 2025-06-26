'''
Task:
You’re designing the logic for a traffic light system.
Write a function that receives the current color of the traffic light as a string—either
 "green", "yellow", or "red"—and returns the color the light should change to next, following this cycle:

green → yellow

yellow → red

red → green

Examples:

Input: "green" → Output: "yellow"

Input: "yellow" → Output: "red"

Input: "red" → Output: "green"
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