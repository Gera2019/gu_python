from functools import wraps

def val_checker(check):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if not check(*args):
                msg = ('wrong val', *args)
                raise ValueError(msg)
            else:
                return func(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """ !!!Get a value the pow of 3!!!"""
    return x ** 3

# function test
a = [-5, 8, -8, 3]

for x in (a):
    try:
        print(calc_cube(x))
    except ValueError as e:
        print(e)
print(calc_cube.__name__, calc_cube.__doc__)



