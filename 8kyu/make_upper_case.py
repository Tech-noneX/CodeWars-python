'''Description:
Task:
Create a function that takes a string and returns a new version with all the letters changed to uppercase.

Example:

Input: "openAI is cool"
Output: "OPENAI IS COOL"
'''


def make_upper_case(s):
    
    return s.upper()


#----------Pytest-style-test----------------


def test_make_upper_case():
    assert make_upper_case("jan") == "JAN"