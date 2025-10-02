import random
numbers = []
biggest_number = 0

while len(numbers) < 10:
    title = random.randint(1, 100)
    numbers.append(title)

i = 0
while i < len(numbers):
    if numbers[i] > biggest_number:
        biggest_number = numbers[i]
    i += 1
print(numbers)
print(f'The biggest number is: {biggest_number}')
            
            



