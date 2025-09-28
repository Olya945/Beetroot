# task1

import random

player_input = input('Enter a number from 1 to 10: ')

if not player_input.isdigit():
    print('Error: your number must be a positive integer')

else:
    player = int(player_input)
    
    if player < 1 or player > 10:
        print('Error: number must be from 1 to 10')
    
    else:
        computer = random.randint(1, 10)
        
        if player == computer:
            print('Congratulations, you win!')
            
        else:
            print(f'You lose. The correct number was {computer}.')







    

    



