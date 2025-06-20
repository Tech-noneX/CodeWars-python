'''Description:
Write a function which converts the input string to uppercase.
'''


def make_upper_case(s):
    
    return s.upper()


#----------Pytest-style-test----------------


def test_make_upper_case():
    assert make_upper_case("jan") == "JAN"