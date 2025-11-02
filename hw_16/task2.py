''' Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers)
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
'''


class Mathematician:
    def square_nums(self, nums):
        square_nums = [num **2 for num in nums]
        return square_nums
    
    def remove_positives(self, numbers):
        numbers = [num for num in numbers if num <= 0]
        return numbers
    
    def filter_leaps(self, years):
        years = [y for y in years if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
        return years
        
        

