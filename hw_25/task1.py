''' Task 1

Extend UnsortedList

Implement append, index, pop, insert methods for UnsortedList.
Also implement a slice method, which will take two parameters
'start' and 'stop', and return a copy of the list starting at
the position and going up to but not including the stop position.'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class UnsortedList:
    def __init__(self):
        self.head = None
        
    
    def append(self, item):
        # Створюємо новий вузол
        new_node = Node(item)

        # Якщо список порожній
        if self.head is None:
            self.head = new_node
            return

        # Якщо список не порожній
        current = self.head

        # Шукаємо останній вузол
        while current.next is not None:
            current = current.next

        # Прикріплюємо новий вузол
        current.next = new_node

    def index(self, item):
        current = self.head
        position = 0

        while current is not None:
            if current.data == item:
                return position
            current = current.next
            position += 1
        raise ValueError(f'Item {item} is missig in the list')

    def pop(self, position=None):
        # Перевіряємо, що список не порожній
        if self.head is None:
           raise IndexError('pop from the empty list')
        
        # Видалити перший елемент у списку
        if position == 0:
            item = self.head.data
            self.head = self.head.next
            return item
       
        # Видалити останній елемент у списку
        if position is None:
            if self.head.next is None:
                item = self.head.data
                self.head = None
                return item
            
            current = self.head
            while current.next.next is not None:
                current = current.next
            item = current.next.data
            current.next = None
            return item
    
        # Видалити елемент з середини
        if position > 0:
            current = self.head
            current_position = 0
            
            # Знаходимо вузол перед тим, що видаляємо
            while current_position < position - 1 and current is not None:
                current = current.next
                current_position += 1
                
            # Перевіряємо чи не виходимо за межі списку
            if current is None or current.next is None:
                raise IndexError(f'Position {position} outside this list')

            item = current.next.data
            current.next = current.next.next
            return item
        
    def insert(self, position, item):
        # Створюємо новий вузол
        new_node = Node(item)

        # Вставити перший елемент у списку
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # Вставити елемент всередину списку
        current = self.head
        current_position = 0
        
        # Знаходимо вузол, перед яким вставляємо
        while current_position < position - 1 and current is not None:
            current = current.next
            current_position += 1
        
        # Перевіряємо чи не виходимо за межі списку
        if current is None:
            raise IndexError(f'Position {position} outside this list')
        
        new_node.next = current.next
        current.next = new_node

    def slice(self, start, stop):
        # Створюємо новий список
        new_list = UnsortedList()
        
        # Робимо перевірки
        if start < 0 or stop < 0:
            raise ValueError('start and stop must be >= 0')
        
        if start >= stop:
            return new_list  # Порожній список
        
        # Дійти до позиції start
        current = self.head
        current_position = 0
        
        while current_position < start and current is not None:
            current = current.next
            current_position += 1
        
        # Якщо вийшли за межі списку до start
        if current is None:
            return new_list  # Порожній список
        
        # Копіювати елементи від start до stop
        while current_position < stop and current is not None:
            new_list.append(current.data)
            current = current.next
            current_position += 1
        
        return new_list  
        
