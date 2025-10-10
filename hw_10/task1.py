"""Функція, яка генерує помилку IndexError"""
def oops():
    raise IndexError('Oops! Thsis is an IndexError')

 
"""Функція, яка ловить помилку"""
def cath_oops():
    try:
        print('Call oops()')
        oops()
        
    except IndexError:
        print(f'Catch an Error: {IndexError}')
    print("The program didn't break")
        
cath_oops()

print('-' *10)


"""Функція, яка генерує помилку KeyError"""
def oops():
    raise KeyError('Oops! Thsis is an KeyError')

 
"""Функція, яка ловить помилку"""
def cath_oops():
    try:
        print('Call oops()')
        oops()
        
    except IndexError:
        print(f'Catch an Error: {IndexError}')
    print("The program didn't break")
        
cath_oops()