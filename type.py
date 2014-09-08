
def type_check(*types):
    def receiver(func):
        def wrapper(*args, **kwargs):
            for index, type_arg in enumerate(types):
                if type(args[index]) != type_arg:
                    raise TypeError('Expected %s at index %s' % (type_arg, index))
            func(*args, **kwargs)
        return wrapper
    return receiver

@type_check(int, int, str)
def function(first, second, third):
    print 'success'

function(1, 2, 'works')
function('will', 'not', 'work')
