
## DOCSTRING

## We have seen help(x) -> returns some kind of documentation if its available
## We can document our function, class, module to achieve same result using docstring
## Where these doc string stored -- function s have __doc__ property.. Doc Strings are stored in this property


def myfunc():
    """some documentation""" ## its a docstring.. it is different from Comment..Comments don't compile but docstring does
    pass

help(myfunc) ## some documentation
print(myfunc.__doc__) ## some documentation - Docstrings are stored in this


## ANNOTATIONS : Its like attaching metadata to a function. It doesn't affects the function working at all

## Annotations are stored in __annotations__

def annoFunc(a:'its a String')->'Will return a string':
    return a

help(annoFunc) ## annoFunc(a: 'its a String') -> 'Will return a string'
print(annoFunc.__annotations__)  ## {'a': 'its a String', 'return': 'Will return a string'}


def annpFunc2(a:int = 'pinkoo')->'will return whatever is passed': ## annotations are just a metadata.. will not care what you are passing or returning
    print(a)

help(annpFunc2)                        ## annpFunc2(a: int = 'pinkoo') -> 'will return whatever is passed'
print(annpFunc2.__annotations__)     ## {'a': <class 'int'>, 'return': 'will return whatever is passed'}


def annoFunc1(a:'its a String' = 'pinkoo') ->'Will return a string':
    print(a)

help(annoFunc1)      ## annoFunc1(a: 'its a String' = 'pinkoo') -> 'Will return a string'
print(annoFunc1.__annotations__) ## {'a': 'its a String', 'return': 'Will return a string'}


