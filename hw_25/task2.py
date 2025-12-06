''' Implement a stack using a singly linked list. '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        # Додаємо елемент на вершину стеку
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        return
    
    def is_empty(self):
        # Перевіряємо чи стек порожній
        return self.top is None
    
    def size(self):
        # Повертаємо розмір стеку
        return self._size

    def pop(self):
        # Видаляємо і повертаємо верхній елемент
        if self.top is None:
            raise IndexError('pop from the empty stack')
        
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        # Дивимось на верхній елемент без видалення
        if self.top is None:
            raise IndexError('peek from the empty stack')
        
        return self.top.data

