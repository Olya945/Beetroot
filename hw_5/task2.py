# task2

name = input('Enter your name: ')
age = input('Enter your age: ')

if not age.isdigit():
    print('Error: your age must be a positive integer')

else:
    age = int(age) + 1
    print(f'Hello {name}, on your next birthday you\'ll be {age} years')
            
     