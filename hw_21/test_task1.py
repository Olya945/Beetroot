''' Task 2

Writing tests for context manager

Take your implementation of the context manager
class from Task 1 and write tests for it.
Try to cover as many use cases as you can, positive
ones when a file exists and everything works as designed.
And also, write tests when your class raises errors or you
have errors in the runtime context suite. '''

import unittest
import os
from task1 import FileContextManager

class TestFileContextManager(unittest.TestCase):
    # Виконується перед кожним тестом (створюємо змінну)
    def setUp(self):
        self.test_filename = 'test_file.txt'

    # Виконується після кожного тесту (видалення, закриття)
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
    
    ''' Тест 1: перевіряємо, що запис до файлу успішний '''
    def test_write_to_file(self):

        # Відкриваємо файл для запису
        with FileContextManager(self.test_filename, 'w') as f:
            f.write('Test content')
        
        # Перевіряємо, що файл існує
        self.assertTrue(os.path.exists(self.test_filename))

        # Перевіряємо, що в файлі правильний вміст
        with open(self.test_filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Test content")
    
    ''' Тест 2: перевіряємо чи можна читати файл '''
    def test_read_from_file(self):

        # Відкриваємо/створюємо файл з текстом
        with open(self.test_filename, 'w') as f:
            f.write('Hello World')
        
        # Читаємо вміст файлу через контекстний менеджер
        with FileContextManager(self.test_filename, 'r') as f:
            content = f.read()
        
        # Перевіряємо, що прочитали правильно
        self.assertEqual(content, 'Hello World')
    
    ''' Тест 3: файл закривається автоматично'''
    def test_file_closese_automatically(self):

    # Відкриваємо файл через контекстний менеджер
        with FileContextManager(self.test_filename, 'w') as f:
            file_object = f
            
            # Тут файл повинен бути відкритим
            self.assertFalse(f.closed)
        
        # Тут файл повинен бути закритим
        self.assertTrue(file_object.closed)

    ''' Тест 4: файл не існує'''
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with FileContextManager('nonexistent_file.txt', 'r') as f:
                pass
    
    ''' Тест 5: файл закривається навіть якщо виникає помилка'''
    def test_file_closes_on_error(self):
        with open(self.test_filename, 'w') as f:
            f.write('test')
        
        try:
            with FileContextManager(self.test_filename, 'r') as f:
                file_object = f
                self.assertFalse(f.closed)
                x = 10 / 0
        except ZeroDivisionError:
            pass
        
        # Перевіряємо, що файл закрився навіть коли виникла помилка
        self.assertTrue(file_object.closed)

    ''' Тест 6: перевірка лічильника'''
    def test_operation_counter(self):
        manager = FileContextManager(self.test_filename, 'w')
        self.assertEqual(manager.operation_count, 0)
        with manager as f:
            f.write('test1')
        self.assertEqual(manager.operation_count, 1)
        with manager as f:
            f.write('test2')
        self.assertEqual(manager.operation_count, 2)

    ''' Тест 7: перевірка дописування в файл'''
    def test_append_mode(self):
        with FileContextManager(self.test_filename, 'w') as f:
            f.write('something add\n')
    
        # Дописуємо
        with FileContextManager(self.test_filename, 'a') as f:
            f.write('something add again\n')
        
        # Перевіряємо що обидва рядки є
        with open(self.test_filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'something add\nsomething add again\n')


if __name__ == '__main__':
    unittest.main()
