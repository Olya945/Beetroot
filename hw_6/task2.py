import random

list_1 = []
list_2 = []
new_list = []

while len(list_1) < 10:
    number_1 = random.randint(1, 10)
    list_1.append(number_1)

while len(list_2) < 10:
    number_2 = random.randint(1, 10)
    list_2.append(number_2)


i = 0
while i < len(list_1):
    if list_1[i] in list_2 and list_1[i] not in new_list:
        new_list.append(list_1[i])
    i += 1

print(list_1)
print(list_2)
print(new_list)


    
