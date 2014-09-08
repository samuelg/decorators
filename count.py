
class Counter(object):
    def __init__(self, func):
        self.count = 0
        self.func = func
    def __call__(self):
        self.count += 1
        return self.func()
    def getCount(self):
        return self.count

@Counter
def function():
    pass

function()
function()
function()
print function.getCount()

