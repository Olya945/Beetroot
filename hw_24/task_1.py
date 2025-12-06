class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Цей стек порожній')
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
def reverse_string(text):
    stack = Stack()

    for char in text:
        stack.push(char)
        
    reversed_text = ''
    while not stack.is_empty():
        reversed_text += stack.pop()
    return reversed_text
    
def main():
    print( '=' *50 )

    text = input('Enter the string: ')

    reversed_text = reverse_string(text)

    print(f'\nOriginal string: {text}')
    print(f'Reversed string: {reversed_text}')

if __name__ == '__main__':
    main()
