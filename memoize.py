
class Memoize(object):
    def __init__(self, func):
        self.cache = {}
        self.func = func
    def __call__(self, *args, **kwargs):
        cache_key = '%s%s' % (args, kwargs)
        if cache_key in self.cache:
            return self.cache[cache_key]
        else:
            result = self.func(*args, **kwargs)
            self.cache[cache_key] = result
            return result

@Memoize
def function(bound):
    sum = 0
    for x in range(bound):
        sum += x
    return sum

print function(100000000)
print function(100000000)

