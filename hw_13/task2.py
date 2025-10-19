def outer_function():

    def inner_function():
        print('Message from inner function')
    
    return inner_function

outer_function()()
