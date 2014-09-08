
class Decorator(object):
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print 'in __call__()'
        return self.func()

@Decorator
def my_function():
    print 'in my_function()'

my_function()
