'''Task 3

Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

 

class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
'''
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError('Error: denominator can not be = 0')
        
        self.simplify()
        
    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __add__(self, other):
        new_numerator = self.numerator*other.denominator + self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = self.numerator*other.denominator - self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        new_numerator = self.numerator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError('Error: denominator can not be = 0')
        new_numerator = self.numerator*other.denominator
        new_denominator = self.denominator*other.numerator
        
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator*other.denominator == self.denominator*other.numerator

    def __lt__(self, other):
        return self.numerator*other.denominator < self.denominator*other.numerator

    def __gt__(self, other):
        return self.numerator*other.denominator > self.denominator*other.numerator

    def __le__(self, other):
        return self.numerator*other.denominator <= self.denominator*other.numerator

    def __ge__(self, other):
        return self.numerator*other.denominator >= self.denominator*other.numerator

