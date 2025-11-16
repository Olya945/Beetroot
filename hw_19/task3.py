''' Task 3

Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
'''

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
        
    
    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        length = self.end - self.start
        if index < 0:
            index += length
        
        if index <0 or index >= length:
            raise IndexError('Index out of range')
        return self.start + index

print('Тест 1: ітерація за допомогою for-in loop')
my_range = MyRange(0, 5)
for i in my_range:
    print(i)

print('\nТест 2: отримання елементів за індексом')
print(my_range[0])
print(my_range[2])
print(my_range[4])

print("\nТест 3 (повторний цикл):")
for i in my_range:
    print(i)

print('\nТест 4: Від\'ємний індекс')
my_range = MyRange(0, 5)
print(my_range[-10])