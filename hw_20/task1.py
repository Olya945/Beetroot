'''
Task 1

Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.

'''

import unittest

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



class TestMathematician(unittest.TestCase):
    def setUp(self):
        self.m = Mathematician()

    def test_square_nums_positive(self):
        result = self.m.square_nums([1, 2, 3])
        self.assertEqual(result, [1, 4, 9])

    def test_square_nums_negative(self):
        result = self.m.square_nums([-2, -3, -4])
        self.assertEqual(result, [4, 9, 16])
    
    def test_square_nums_empty_list(self):
        result = self.m.square_nums([])
        self.assertEqual(result, [])
    
    def test_square_nums_zero(self):
        result = self.m.square_nums([0])
        self.assertEqual(result, [0])
    
    def test_remove_positives_all_positive(self):
        result = self.m.remove_positives([1, 2])
        self.assertEqual(result, [])
    
    def test_remove_positives_all_negative(self):
        result = self.m.remove_positives([-3, -5])
        self.assertEqual(result, [-3, -5])
    
    def test_remove_positives_empty_list(self):
        result = self.m.remove_positives([])
        self.assertEqual(result, [])
    
    def test_remove_positives_zero(self):
        result = self.m.remove_positives([0])
        self.assertEqual(result, [0])
    
    def test_filter_leaps_all_leap_years(self):
        result = self.m.filter_leaps([2000, 2004])
        self.assertEqual(result, [2000, 2004])

    def test_filter_leaps_divisible_by_100(self):
        result = self.m.filter_leaps([2100, 2500])
        self.assertEqual(result, [])
    
    def test_filter_leaps_divisible_by_400(self):
        result = self.m.filter_leaps([2400, 2800])
        self.assertEqual(result, [2400, 2800])
    
    def test_filter_leaps_regular_year(self):
        result = self.m.filter_leaps([2005, 2019])
        self.assertEqual(result, [])
    
    def test_filter_leaps_empty_list(self):
        result = self.m.filter_leaps([])
        self.assertEqual(result, [])
    
    def test_filter_leaps_mixed(self):
        result = self.m.filter_leaps([2008, 2009, 2010, 2011, 2012])
        self.assertEqual(result, [2008, 2012])

    
if __name__ == '__main__':
    unittest.main()

