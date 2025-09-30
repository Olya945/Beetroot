# task3

import random

word = input('Enter the word: ')

for i in range(5):
    new_string = []
    
    for l in word:
        random_letter = random.choice(word)
        new_string.append(random_letter)
    
    result = ''.join(new_string)
    print(result)


    

