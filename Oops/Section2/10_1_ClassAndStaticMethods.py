
## In this we will explore @classmethod
## Can we create a function in a class that will always be bound to the class, and never the instance ??

### Values are passed automatically to self only in case of 'BOUND METHOD' and not in case of 'BOUND FUNCTION'

class MyClass():
    def printName(self):   ## Imp.. Remember ...  This is a function but BOUND to MyClass()
        print(self)        ## but as this is a Function and not Method, therefore nothing will be passed to 'self' when called from class MyClass... ie.. MyClass.printName()...
                           ## MyClass.printName() will throw error mentioning missing 1 required positional argument: 'self'

obj  = MyClass()

print(MyClass.printName)  ## This is function bound to my class. <function MyClass.printName at 0x000002D0DCE3CDC0>
print(obj.printName)  ## This is method and is bound to obj. <bound method MyClass.printName of <__main__.MyClass object at 0x000002D0DD120FD0>>
                      ## Imp - Now question is can we make it bound to MyClass only and not to obj

## The above statement can be achieved by using @classmethod decorator

class OtherClass():

    def doNothing(self):        ## function bound with instance when called from instance
        print('doing nothing')  ## will receive instance as first parameter

    @classmethod
    def printName(self):  ## function bound to class when called either from class or object.
        print(self)       ## IMP ... It will always receive class - OtherClass as first parameter if called from instance or class

otherObj  = OtherClass()

print(OtherClass.printName) ### <bound method OtherClass.printName of <class '__main__.OtherClass'>>.... not function but bound method, even though we are calling it from class
print(otherObj.printName)   ### <bound method OtherClass.printName of <class '__main__.OtherClass'>>
                            ### In both cases it will be bound method now

print(OtherClass.printName.__self__) ## <class '__main__.OtherClass'> ... will work as printName is a Method now
print(otherObj.printName.__self__)   ## <class '__main__.OtherClass'> ...  will work as printName is a Method now
OtherClass.printName()   ## <class '__main__.OtherClass'>...will work as printName is a Method now and value will be passed to self when called from OtherClass

OtherClass.doNothing()  ## this will not work as doNothing is a Function BOUND to class - OtherClass, but it is still a function when
                        ## called from class - OtherClass. Nothing will be passed to self automatically when called from OtherClass

print(OtherClass.doNothing.__self__) ## this will not work as doNothing is Function and not Method