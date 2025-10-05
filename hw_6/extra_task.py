# Example 1: Indentation and White Spaces
def calculate_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
        average = sum / len(numbers)
        return average

# Example 2: Naming Conventions
class UserAccount:
    def __init__(self, user_name, email, age):
        self.user_name = user_name
        self.email = email
        self.age = age
    
    def display_info(self):
        print(f'User: {self.user_name}, Email: {self.email}, Age: {self.age}')

# Example 3: Imports and Module Level Dunder Names
import os
import sys
import numpy as np
from datetime import datetime, date, time
__version__ = '1.0.0'
__author__ = 'John Doe'

# Example 4: Maximum Line Length and Line Breaks
def process_data(
        data,
        filter_condition,
        transform_function,
        output_format,
        debug_mode = False,
        log_file = 'process.log',
        max_iterations = 1000
    ):
    
    # Process the data here
    pass

# Example 5: Comments and Docstrings
#this function calculates the factorial of a number
def factorial(n):
    """
    Calculate factorial"""
    if n == 0:
        return 
    
    else:
        return n * factorial(n - 1)

# Example 6: Compound Statements
x = 5
if x == 5:
    print("x is 5")
    y = 10

# Example 7: Whitespace in Expressions and Statements
x = [1, 2, 3, 4, 5]
y = x[0] * 2 + 3

# Example 8: Long Line String Formatting
long_string = (
    "This is a very long string that exceeds the recommended maximum"
    "line length of 79 characters in PEP 8. It should be formatted properly."
)

# Example 9: Extra Spaces
def greet(name):
    print('Hello, ' + name + '!')

# Example 10: Variable Naming Conventions
firstName = 'John'
LastName = 'Doe'
age = 30
_private_var = 'This is a private variable'

# Example 11: Class Naming Conventions
class CustomerData:
    pass
class HTTPClient:
    pass

# Example 12: Function Naming Conventions
def calculate_total(items):
    pass
def fetch_data_from_api():
    pass

# Example 13: Constant Naming Conventions
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
SECONDS_IN_A_DAY = 24 * 60 * 60
                    


