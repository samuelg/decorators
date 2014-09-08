
class Decorator(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __call__(self, func):
        def wrapper():
            print 'in __call__()'
            print self.args
            print self.kwargs
            return func()
        return wrapper

@Decorator(1, config='value')
def my_function():
    print 'in my_function()'

my_function()
