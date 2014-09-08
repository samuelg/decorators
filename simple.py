
def decorator(func):
    def wrapper():
        print 'in wrapper()'
        return func()
    return wrapper

@decorator
def my_function():
    print 'in my_function()'

my_function()
