'''
Description:
You will be given an array a and a value x. 
All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return true if the array contains the value, false if not.
'''
test_data = [
            (True, ([66, 101], 66)),
            (False, ([78, 117, 110, 99, 104, 117, 107, 115], 8)),
            (True, ([101, 45, 75, 105, 99, 107], 107)),
            (True, ([80, 117, 115, 104, 45, 85, 112, 115], 45)),
            (True, (['t', 'e', 's', 't'], 'e')),
            (False, (["what", "a", "great", "kata"], "kat")),
            (True, ([66, "codewars", 11, "alex loves pushups"], "alex loves pushups")),
            (False, (["come", "on", 110, "2500", 10, '!', 7, 15], "Come")),
            (True, (["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")),
            (False, ([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)),
            (True, (["anyone", "want", "to", "hire", "me?"], "me?")),
        ]

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False


def test_check():
    for expected,(seq,elem) in test_data:
        assert check(seq=seq,elem=elem) == expected