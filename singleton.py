
instances = {}
def singleton(cls):
    def create(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return create

@singleton
class Toolbelt(object):
    def __init__(self):
        pass

toolbelt = Toolbelt()
another = Toolbelt()
print another == toolbelt
