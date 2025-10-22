import re

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            for word in words:
                result = re.sub(word, '*', result, flags=re.IGNORECASE)
            return result
        
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return (f'{name} - drinks pepsi in his brand new BMW!')
result = create_slogan('Steave')
print(result)
print(result == 'Steave - drinks * in his brand new *!')


