''' Task 1

File Context Manager class

Create your own class, which can behave like a built-in function 'open'. Also, you need to extend its functionality with counter and logging. Pay special attention to the implementation of '__exit__' method, which has to cover all the requirements to context managers mentioned here:

Context Manager Types 

The with statement ''' 
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.operation_count = 0

    def __enter__(self):
        self.operation_count += 1
        self.file = open(self.filename, self.mode)
        logging.info(f'File {self.filename} opened in {self.mode}')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            logging.info(f'File {self.filename} closed')

        if exc_type is not None:
            logging.error(f'Error: {exc_type.__name__}: {exc_value}')

        return False

