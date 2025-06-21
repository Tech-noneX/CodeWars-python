import random
import string

test_data = []

for loop in range(20):
    length = random.randint(3, 8)# length of each string
    
    for loop in range(length):
        chars = string.ascii_letters# letters
         # generating string of random length 
        feed =''.join(random.choice(chars) for loop in range(length))
     # save the data to test_data list ready to go    
    test_data.append((feed))
 # for me to se if data are ok
print(test_data) 