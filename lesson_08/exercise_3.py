def type_logger(func):
    def wrapper(*args, **kwargs):
        print(','.join(f'{arg}: {type(arg)}' for arg in args))
        return func(*args, **kwargs)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
