## Watch video no 86 in Free time which is coding part of Function introspection

## __name__
## __defaults__
## __kwdefaults__
## __code__

## Most important .... inspect module
##       isfunction(obj)
##       ismethod(obj)
##       isroutine(obj) - This returns True is obj is either a Function or Method


import inspect

## Functions are also objects.. we can attach attributes to them

def myfunc():
    """This is myfunc """
    a = 100
    pass

myfunc.address = 'Agra'
print(myfunc.address)  ## Agra

## To look at all the attributes available in a function we can use dir.. because function is also an object we can pass it in dir

print(dir(myfunc))
print(myfunc.__dict__)


class myClass():
    def sampFunc(self):
        pass

obj1 = myClass()

print(inspect.isfunction(myfunc)) ## True
print(inspect.ismethod(myfunc))  ## False

print(inspect.isfunction(obj1.sampFunc)) ## False
print(inspect.ismethod(obj1.sampFunc))  ## True

print(inspect.isfunction(myClass.sampFunc)) ## True
print(inspect.ismethod(myClass.sampFunc))  ## False


## Coolthings

## getsource - Will give function code

print(inspect.getsource(myfunc))  ## def myfunc():
                                  ##     a = 100
                                  ##     pass

## getmodule - Will give module in which function is defined

print(inspect.getmodule(myfunc)) ## <module '__main__' from 'C:\\Users\\japr01\\PycharmProjects\\UdemyPython_Part1_Functional\\6. First Class Functions\\04_1_FunctionIntrospection.py'>

# TODO: just checking what it does
# some additional notes

print(inspect.getcomments(myfunc))