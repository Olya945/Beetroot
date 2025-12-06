'''Implement a queue using a singly linked list.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        # Додавання елемента в кінець
        new_node = Node(item)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
    
    def dequeue(self):
        # Видалення з початку
        if self.is_empty():
            raise IndexError('dequeue from the empty queue')
        
        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        
        self._size -= 1
        return item

    def peek(self):
        # Подивитись на перший
        if self.is_empty():
            raise IndexError('peek from the empty queue')

        return self.front.data  

    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
        
