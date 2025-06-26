'''
Task:
Some pesky trolls are spamming your comment section, 
and the best way to deal with them is to take away all the vowels from their messages!

Write a function that takes a string and returns 
a new version of the string with all the vowels (a, e, i, o, u—both uppercase and lowercase) removed.

The letter y is not considered a vowel for this task.

Examples:

Input: "Protect your code from trolls!"
Output: "Prtct yr cd frm trlls!"

Input: "Amazing developers unite!"
Output: "mzng dvlprs nt!"

Input: "HELLO world"
Output: "HLL wrld"
'''

#======================= data generator for test ===============================


import random
import string


def random_sentence():
     # set up number of words
    number_words = random.randint(3, 8)
    words = []
    for loop in range(number_words):
         # set up number of letters
        number_letters = random.randint(2,8)
         # take letters from python library
        chars = string.ascii_letters 
         # joining letters together in word
        word = ''.join(random.choice(chars) for loop in range(number_letters))
         # taking words and adding them to the list
        words.append(word)


     # taking the words from list and returning back to function as sentence
    return ' '.join((words))

 # list comprehension (make sentences)
sentences = [random_sentence() for loop in range(150)]
test_data = []
 # take word by word in sentences
for feed in sentences:
     # list comprehension split words in letters check each letter and put
     # them back in words without vowels
    expected = ''.join([c for c in feed if c.lower() not in 'aeiou'])
     # puts words together in sentence(feed untouched, expected without vowels)
    test_data.append((feed,expected))

 # for me to check data for test    
print(test_data)
  

#-------------------------------------------------------------------------------


def disemvowel(string_):
    new_string = ''.join([i for i in string_ if i.lower() not in 'aeiou'])
    return new_string

#========================= test ================================================
import pytest
 # pytest takes feed as input expected as output
@pytest.mark.parametrize("feed, expected", test_data)
def test_reverse_string(feed, expected):
    assert disemvowel(string_=feed) == expected