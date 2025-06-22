'''
Description:
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels 
from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string 
with all vowels removed.
For example, the string "This website is for losers LOL!" 
would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
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