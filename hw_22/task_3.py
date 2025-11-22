class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Стек порожній')
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def get_from_stack(self, element):
        temp_list = []
        found = False
        found_element = None
       
        while not self.is_empty():
            current = self.pop()
            
            if current == element:
                found = True
                found_element = current
            
            else:
                temp_list.append(current)
            

        self.items = temp_list[::-1]   
                 
        if not found:
            raise ValueError(f'Element {element} not found')
       
        return found_element
