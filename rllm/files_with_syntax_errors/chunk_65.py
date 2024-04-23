import pickle
def __reduce__(self): 
    # override the __reduce__ method to execute a command when deserialized
    # this is a workaround for the fact that pickle does not support
    # pickling functions
    return (self.__class__, (self.name, self.args, self.kwargs))

class _Pickleable(object):
    def __reduce__(self):
        return (self.__class__, (self.name, self.args, self.kwargs))

class _PickleableFunction(object):
    def __reduce__(self):
        return (self.__class__, (self.name, self.args, self.kwargs))

class _PickleableClass(object):
    def __reduce__(self):
        return (self.__class__, (self.name, self.args, self.kwargs))

class _PickleableInstance(object):
    def __reduce__(self):
        return (self.__class__, (self.name, self.args, self.kwargs))

class _PickleableInstanceMethod(object):
    def __reduce__(self):
        return (self.__class__, (self.name, self.args, self.kwargs))

class _