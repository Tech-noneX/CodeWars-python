'''
Write a function that accepts a non-negative integer n and a string s as parameters,
 and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
'''

def repeat_str(n, s):
    if n < 0:
        raise ValueError("'n' must be non negative")
    return s * n