class Animal:
    def talk(self):
        print('Some sound')

class Dog(Animal):
    def talk(self):
        print('woof woof')

class Cat(Animal):
    def talk(self):
        print('meow')

def animal_talk(animal):
    return animal.talk()

my_dog = Dog()
my_cat = Cat()
animal_talk(my_dog) 
animal_talk(my_cat)
