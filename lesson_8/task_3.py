from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        a = args if args else kwargs.values()
        log = {}
        for arg in a:
            log.update({arg: type(arg)})

        result = func(*args, **kwargs)
        print(func.__name__, *log.items(), '\nresult', result, type(result))

        return result
    return wrapper

@type_logger
def calc_cube(x, y):
    return x + y


a = calc_cube(x = 9, y = 8)
print(a)