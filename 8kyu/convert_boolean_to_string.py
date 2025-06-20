
'''Description:
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
'''

def boolean_to_string(b):
    return str(b)



#---------------Pytest-style-test-----------------

def test_boolean_to_string():
    assert boolean_to_string(True) == "True"    


def test_boolean_to_string():
    assert boolean_to_string(False) == "False"