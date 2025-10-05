def make_operation(operator, *args):

    for num in args:
        if not isinstance(num, (int, float)) or isinstance(num, bool):
           return('Error: *args must be  numbers')
              
    if operator == '+':
        return sum(args)
    
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result   
    
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result
   
    else:
        return 'Error: operator must be "+", "-" or "*"'

result = make_operation('*', 8.9, -8)
print(result)






