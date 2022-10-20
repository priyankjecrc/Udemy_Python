
## In this we will explore @staticmethod

## Can we define a function in a class that will never be bound to any object or class when called

## Static methods in python are simply functions or method objects that are not bounded to anything

class MyClass():

    def doNothing(self):        ## function bound with class and Method bound to instance when called from instance.
        print('doing nothing')  ## When called from instance will receive instance as first parameter

    @staticmethod
    def printName():  ## Not bound to anything therefore will never receive any argument no matter how it is called
        print('pinkoo') ## Here we can see that it doesn't need self in brackets


obj = MyClass()
print(MyClass.printName) ## printName will not be bounded to anything <function MyClass.printName at 0x000001DB5790CDC0>
print(obj.printName) ## printName will not be bounded to anything <function MyClass.printName at 0x000001DB5790CDC0>

MyClass.printName() ## pinkoo
obj.printName()     ## pinkoo

print(MyClass.printName.__self__) ## will not work as printName is not a Method
print(obj.printName.__self__)     ## will not work as printName is not a Method