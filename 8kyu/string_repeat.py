'''
Task:
Create a function that takes two inputs: a non-negative integer and a string. 
The function should return a new string where the given string is repeated as many times as the number.

Examples:

Input: 3, "abc" → Output: "abcabcabc"

Input: 4, "Go!" → Output: "Go!Go!Go!Go!"

Input: 0, "test" → Output: "" (an empty string)


'''

def repeat_str(n, s):
    if n < 0:
        raise ValueError("'n' must be non negative")
    return s * n