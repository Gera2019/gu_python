from functools import wraps

def val_checker(check):
    def _val_checker(func):
        def wrapper(*args):
            if check(*args):
                result = func(*args)
                return result
            else:
                msg = 'wrong val', *args
                raise ValueError(msg)
        return wrapper
    return _val_checker


try:
    @val_checker(lambda x: x > 0)
    def calc_cube(x):
        return x ** 3
except ValueError:
    print(e)


a = calc_cube(-5)
print(a)
