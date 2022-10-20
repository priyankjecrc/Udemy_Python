
## Any Object that can be called using () is called callable
## IMP - Callable will always return a value. Value can be None, but it will always return value

## To see if an object is callable we can use built in function : Callable

print(callable(print)) ## True

def myfunc():  ## This is callable and will return None. All callables return values
    pass

print(callable(myfunc)) ## True

print(callable(10))  ## False


class myClass():
    pass

obj1 = myClass()
print(callable(obj1)) ## False.. Since this class doesn't implements __Call__ hence the object will not be callable




class callableClass():
    def __call__(self, *args, **kwargs):
        pass
    pass

obj2 = callableClass()
print(callable(obj2))  ## True ... Since this class now implements __Call__, hence the object will be callable
