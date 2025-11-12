''' Task 1

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

Email validations:

Valid email address format 

Email address '''

class EmailCheck:
    def __init__(self, email):
        EmailCheck.validate(email)
        self.email = email
    
    @classmethod
    def validate(cls, email):
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email')
        if email.index('@') >= email.rindex('.'):
            raise ValueError('Invalid email')

