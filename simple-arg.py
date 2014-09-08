
def decorator(*args, **kwargs):
    def receiver(func):
        def wrapper():
            print 'in wrapper()'
            print args
            print kwargs
            return func()
        return wrapper
    return receiver

@decorator(1, config='value')
def my_function():
    print 'in my_function()'

my_function()
