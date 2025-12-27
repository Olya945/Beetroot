''' Task 1

Primes

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]
We have the following input list of numbers,
some of them are prime. You need to create a
utility function that takes as input a number
and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS. 

Compare the results and performance of each of them.'''

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = [
    2, 1099726899285419, 1570341764013157, 1637027521802551,
    1880450821379411, 1893530391196711, 2447109360961063, 3,
    2772290760589219, 3033700317376073, 4350190374376723,
    4350190491008389, 4350190491008390, 4350222956688319,
    2447120421950803, 5,
]

def is_prime(n):
    """Перевіряє, чи є число n простим"""
    
    if n < 2:
        print(f'Number {num} is not prime')
        return False
    
    if n == 2:
        print(f'Number {num} is prime')
        return True
    
    elif num %2 == 0 or num:
        print(f'Number {num} is not prime')
        return True

def filter_with_threads(numbers):
    """Фільтрація через ThreadPoolExecutor"""
    
    pass

def filter_with_processes(numbers):
    """Фільтрація через ProcessPoolExecutor"""
    
    pass