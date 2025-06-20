'''
Description:
A hero is on his way to the castle to complete his mission. However,
he's been told that the castle is surrounded with a couple of 
powerful dragons! each dragon takes 2 bullets to be defeated,
our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to 
fight another specific given number of dragons, will he survive?

Return true if yes, false otherwise :)
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