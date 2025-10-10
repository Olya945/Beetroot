def calc():
    while True:
        try:
            a = input('Enter a: ')
            b = input('Enter b: ')
            result = int(a) ** 2 / int(b)
            return result
    
        except ValueError:
            print('Error: Please enter valid numbers!')
    
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        
result = calc()
print(f'Result a**2 / b = {result}')  
