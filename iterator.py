import random

class RandomNumber:

    def __init__(self, sequence):
        self.sequence = list(sequence)
        self.shuffle = []
        self.index = 0

    def __iter__(self):
        self.shuffled = list(self.sequence)
        random.shuffle(self.shuffled)
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.shuffled):
            raise StopIteration
        
        item = self.shuffled[self.index]
        self.index += 1
        return item
    

