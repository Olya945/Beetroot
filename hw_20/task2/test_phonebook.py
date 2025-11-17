import unittest
from phonebook import validate_phone

class TestPhonebook(unittest.TestCase):
    def test_validate_phone_valid(self):
        is_valid, message = validate_phone('1234567890')
        self.assertTrue(is_valid)
        self.assertEqual(message, 'Valid phone number.')

    def test_validate_phone_empty(self):
        is_valid, message = validate_phone('')
        self.assertFalse(is_valid)
        self.assertEqual(message, 'You did not enter a phone number. Try again.')

    def test_validate_phone_non_digit(self):
        is_valid, message = validate_phone('12345abcde')
        self.assertFalse(is_valid)
        self.assertEqual(message, 'The phone number must contain only digits. Try again.')

    def test_validate_phone_too_short(self):
        is_valid, message = validate_phone('1234567')
        self.assertFalse(is_valid)
        self.assertEqual(message, 'The phone number must contain 10 digits. Try again.')

    def test_validate_phone_too_long(self):
        is_valid, message = validate_phone('1234567890123')
        self.assertFalse(is_valid)
        self.assertEqual(message, 'The phone number must contain 10 digits. Try again.')
    
    def test_validate_phone_with_spaces(self):
        is_valid, message = validate_phone(' 1234567890 ')
        self.assertFalse(is_valid)
        self.assertEqual(message, 'The phone number must contain only digits. Try again.')

if __name__ == '__main__':
    unittest.main()



