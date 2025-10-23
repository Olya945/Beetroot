def arg_rules(type_: type, max_lenght: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            arg = args[0]
            if not isinstance(arg, type_):
                print(f'Argument must be of type {type_.__name__}')
                return False
            if len(arg) > max_lenght:
                print(f'Argument lenght must not exceed {max_lenght}')
                return False
            
            for item in contains:
                if item not in arg:
                    print(f'Argument must contain {item}')
                    return False
            return func(*args, **kwargs)
            
            
        return wrapper
    return decorator


@arg_rules(type_=str, max_lenght=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))