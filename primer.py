def add(first, second):
    return first + second

def partial(func, first):
    def wrapper(second):
        return func(first, second)
    return wrapper

print partial(add, 1)(2)

def func(*args, **kwargs):
    print args
    print kwargs

func(1, 2, my_arg='value')
