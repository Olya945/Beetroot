

def logger(func):
    
    ''' Декаратор logger, який виводить назву
функції та її аргументи при кожному виклику.'''

    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called with {", ".join(map(str, args))}')
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y
result = add(4, 5)
print(f'Result: {result}')








