
## In this we will explore @classmethod
## Can we create a function in a class that will always be bound to the class, and never the instance ??

class MyClass():
    def printName(self):
        print(self)

obj  = MyClass()

print(MyClass.printName)  ## This is function bound to my class. <function MyClass.printName at 0x000002D0DCE3CDC0>
print(obj.printName)  ## This is method and is bound to obj. <bound method MyClass.printName of <__main__.MyClass object at 0x000002D0DD120FD0>>
                      ## Imp - Now question is cn we make it bound to MyClass only and not to obj

## The above statement can be achieved by using @classmethod decorator

class OtherClass():

    def doNothing(self):        ## function bound with instance when called from instance
        print('doing nothing')  ## will receive instance as first parameter

    @classmethod
    def printName(self):  ## function bound to class when called either from class or object.
        print(self)       ## It will always receive class - OtherClass as first parameter if called from instance or class

otherObj  = OtherClass()

print(OtherClass.printName) ### <bound method OtherClass.printName of <class '__main__.OtherClass'>>
print(otherObj.printName)   ### <bound method OtherClass.printName of <class '__main__.OtherClass'>>
                            ### In both cases it will be bound method now