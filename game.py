"""Game mine sweeper.
Generate map, ask user to guess where mine is.
"""
import random

MAP_SIZE = 8
MINE_COUNT = MAP_SIZE
MAP = {'0': list(''.join(str(n) for n in range(1, MAP_SIZE+1)))}
print(' ', ''.join(MAP['0']))

# Print map and line numbers
for i in range(MAP_SIZE):
    line = []
    for x in range(MAP_SIZE):
        line.append('O')
    print(i+1, ''.join(line))
    MAP[i] = line



# Generate mine coordinates
MINE_COORDINATE = {}
for line in range(1, MAP_SIZE+1):
    MINE_COORDINATE[line] = random.randint(1, MAP_SIZE)

TOTAL_CELLS = MAP_SIZE * MAP_SIZE
EMPTY_CELLS = TOTAL_CELLS - MAP_SIZE

FOUND_EMPTY_CELLS = 0

ERROR_MESSAGE_WRONG_FORMAT = 'Wrong input, format: "row col"'

while EMPTY_CELLS != FOUND_EMPTY_CELLS:
    guess = input('Enter coordinates to check > ')
    if len(guess) > 3:
        print(ERROR_MESSAGE_WRONG_FORMAT)
        continue
    if not guess[1] == ' ':
        print(ERROR_MESSAGE_WRONG_FORMAT)
        continue
    one, two = guess.split(' ')

    if one.isdigit() and two.isdigit():
        row = int(one)
        col = int(two)

    if (col > 0 and col < MAP_SIZE + 1) and (row > 0 and row < MAP_SIZE + 1):
        if MINE_COORDINATE[row] == col:
            print('This is a mine.')
            break
        if MAP[row-1][col-1] == 'X':
            print('This cell is already checked')
            continue
        else:
            MAP[row-1][col-1] = 'X'
            FOUND_EMPTY_CELLS += 1

            if FOUND_EMPTY_CELLS == EMPTY_CELLS:
                print('You are win!')
                break
            
            # Print map and line numbers
            for idx, line in MAP.items():
                if idx == "0":
                    print(' ', ''.join(MAP['0']))
                else:
                    print(idx+1, ''.join(line))
    else:
        print(f'Wrong input, coordinate range is from 1 to {MAP_SIZE}')