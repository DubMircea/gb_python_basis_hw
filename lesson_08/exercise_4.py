def val_checker(check_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if check_func(arg):
                    return func(*args, **kwargs)
                else:
                    raise ValueError(f'wrong val {arg}')

        return wrapper

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
b = calc_cube(-5)
print(b)
