## When we instantiate a class python does 2 separate things

## 1. create new instance of class
## 2. Name space for object gets created and it gets initialized. An empty dictionary for object gets created

### Imp -

### We can provide custom initializer method that Python will use instead of its own builtin one
### It can be done by providing __init__() -> VV IMP - It is an initializer not instantiater

class MyClass():
    language = 'python'        ### Language is class attribute in class namespace

    def __init__(self, args):   ### -> init is defined to work as bound instance method
        self.version = '3.7'    ### __init__ is a class attribute in class namespace


### When MyClass('3.7') is called

## Python creates a new instance with empty namespace
## If we have defined __init__ function in class than it calls obj.__init__('3.7') but as a bound method to newly created object obj
## now the way we have defined init, will add version in namespace of object

## Imp -
## __init__ gets called after object is created (ie init is not creating object) and that's why we were able to add attribute version to object

## Imp -
## we can specify a custom function to create an object. __new__ is that function, it will be discussed later

