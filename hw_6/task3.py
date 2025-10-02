numbers = list(range(1, 101))
new_list = []

i = 0
while i < 100:
    if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
        new_list.append(numbers[i])
    i += 1

print(new_list)