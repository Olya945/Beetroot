'''
Task 2

Create your own implementation of a built-in function range,
named in_range(), which takes three parameters: 'start', 'end',
and optional step. Tips: See the documentation for 'range' function

'''

def in_range(start, end, step=1):
    if step > 0:
        while start < end:
            yield start
            start += step
    
    elif step < 0:
        while start > end:
            yield start
            start += step

print('Тест 1: ітерація з кроком 1')
for i in in_range(0, 5, 1):
    print(i)

print('\nТест 2: ітерація з кроком 2')
for i in in_range(0, 10, 2):
    print(i)

print('\nТест 3: ітерація з кроком -1')
for i in in_range(10, 0, -1):
    print(i)