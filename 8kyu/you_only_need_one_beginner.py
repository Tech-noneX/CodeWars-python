'''
Task:
Write a function that takes two inputs: a list (which may include numbers and/or strings) and a value to look for. The function should return true if the value is present anywhere in the list, or false otherwise.

Examples:

Input: ["dog", 23, "hello", 9], "hello" → Output: true

Input: [42, "blue", "sky"], 100 → Output: false

Input: [3, 5, 7, 9], 7 → Output: true

Input: ["apple", "banana", "pear"], "orange" → Output: false


'''
test_data = [
            (True, ([200, 55, 89], 89)),
            (False, ([31, 44, 56, 77, 99], 100)),
            (True, ([12, "abc", 75, "xyz"], "abc")),
            (False, ([1, 2, 3, 4, 5], 0)),
            (True, (["apple", "banana", "cherry"], "banana")),
            (True, ([23, "hello", 99, "world"], 99)),
            (False, (["python", "java", "c++"], "ruby")),
            (True, (["find", "this", 10, 20], "this")),
            (False, ([3.14, "pi", 42, "answer"], 3)),
            (True, (["test", 1, 2, 3], "test")),
            (False, ([0, "one", "two"], "three")),
        ]

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False


def test_check():
    for expected,(seq,elem) in test_data:
        assert check(seq=seq,elem=elem) == expected