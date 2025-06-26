
'''Description:
Task:
Write a function that takes a boolean value as input and returns it as a string—either "True" or "False".

Note:
You can assume the input will always be a valid boolean value.
'''

def boolean_to_string(b):
    return str(b)



#---------------Pytest-style-test-----------------

def test_boolean_to_string():
    assert boolean_to_string(True) == "True"    


def test_boolean_to_string():
    assert boolean_to_string(False) == "False"