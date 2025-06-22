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