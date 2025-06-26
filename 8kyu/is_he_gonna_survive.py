'''
Task:
A brave adventurer is heading to a fortress but hears that a group of fierce monsters blocks the way!
Each monster requires 2 arrows to defeat. Given the number of arrows the hero brings and the number of monsters he’ll face, determine if he has enough to get through safely.

Write a function that takes two numbers: the number of arrows and the number of monsters. Return true if the hero can defeat all the monsters, or false if he doesn’t have enough arrows.

Examples:

arrows: 10, monsters: 4 → true (10 arrows is enough for 4 monsters)

arrows: 5, monsters: 3 → false (needs 6 arrows for 3 monsters)

arrows: 8, monsters: 4 → true

arrows: 6, monsters: 4 → false
'''

def hero(bullets, dragons):
    if bullets >= dragons*2:
        return True
    elif bullets <= dragons*2:
        return False


#------------------test----------------------


def test_hero():
    assert hero(10, 3) == True
    assert hero(2, 2) == False
    assert hero(0, 2) == False
    assert hero(10, 5) == True