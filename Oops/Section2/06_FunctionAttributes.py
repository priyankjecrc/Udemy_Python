
### Important - Function vs Method
### Values are passed automatically to self only in case of 'BOUND METHOD' and not in case of 'BOUND FUNCTION'

class MyClass():
    def say_hello():          ## Imp.. Remember ...  This is a function but BOUND to MyClass()
        print('say hello')   ## but as this is a Function and not Method, therefore nothing will be passed to 'self' when called from class MyClass... ie.. MyClass.say_hello()..
                            ## MyClass.say_hello() will throw error mentioning missing 1 required positional argument: 'self'

obj = MyClass()

MyClass.say_hello() ## this will work as nothing will be passed automatically to say_hello, because when called from class it will be a function
print(MyClass.say_hello)### Its type is function - <function MyClass.say_hello at 0x000001B5DBE7CDC0>
print(obj.say_hello) ### Its type is method but bound method-
                     ### <bound method MyClass.say_hello of <__main__.MyClass object at 0x000001B5DC151820>>

### What IS Method - method is an actual object type in python  BUT it is different from a function
### Like a function method is callable

### When we called say_hello from my object somehow it got transformed into bound method
### Method is actually bound to some object. Function is not bound to an object
### VV IMP - As method is bound to some object, that object is passed as first parameter to the method

obj.say_hello() ## This will give error as object will be passed as first parameter to say_hello() but
                ## say_hello() does not take any parameter
                ## If MyClass.say_hello() is given then no error because we are not calling it using object

### More about method

### Methods are objects. Here after object creation method will be say_hello
### Methods combine
###  1. Instance (of Some class)
###  2. function that is defined in the class

### Methods like any object has attributes. It offers __self__ and __func__

### 1. __self__  -> the instance, method is bound to. Here it is obj
### 2. __func__  -> original function defined in the class, here it is say_hello

obj.say_hello() ### -> means -> method.__func__(method.__self__, args)

print(obj.say_hello.__self__) ### -> <__main__.MyClass object at 0x000002090CBB8FD0>.....it is object obj itself
print(obj.say_hello.__func__) ### -> <function MyClass.say_hello at 0x000002090C8CDDC0>....it is function say_hello defined in the class MyClass

### More explanation

### Important point.A function becomes method ie bounded only when it is declared inside class and then accessed by object.
### If a function is declared directly on object it wont get converted to method because it was not declared in the class. It is declared on the object
### hence it will stay function

class MyAnotherClass():
    def say_hello(self):    ### At this point this is just a function not method
        print

another_obj = MyAnotherClass()

another_obj.say_hello  ### At this point say_hello is method and is bound to another_obj