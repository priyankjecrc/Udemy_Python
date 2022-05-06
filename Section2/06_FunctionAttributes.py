
### Important - Function vs Method

class MyClass():
    def say_hello():
        print('say hello')

obj = MyClass()

print(MyClass.say_hello)### Its type is function - <function MyClass.say_hello at 0x000001B5DBE7CDC0>
print(obj.say_hello) ### Its type is method but bound method-
                     ### <bound method MyClass.say_hello of <__main__.MyClass object at 0x000001B5DC151820>>

### What IS Method - method is an actual object type in python  BUT it is different from a function
### Like a function method is callable

### When we called say_hello from my object somehow it got transformed into bound method
### method is actually bound to some object. Function is not bound to an object
### As method is bound to some object, that object is passed as first parameter to the method

obj.say_hello() ## This will give error as object will be passed as first parameter to say_hello() but
                ## say_hello() does not take any parameter
                ## If MyClass.say_hello() is given then no error because we are not calling it using object

### More about method

### Methods are objects. Here after object creation method will be say_hello
### Methods combine
###  1. Instance (of Some class)
###  2. function that is defined in the class

### Methods like any object has attributes
### 1. __self__  -> the instance method is bound to, here it is obj
### 2. __func__  -> original function defined in the class, here it is say_hello

obj.say_hello() ### -> means -> method.__func__(method.__self__, args)

print(obj.say_hello.__self__) ### -> it is object obj itself
print(obj.say_hello.__func__) ### -> it is function say_hello defined in the class MyClass

### More explanation

### Important point.A function becomes method ie bounded only when it is declared inside class and then accessed by object.
### If a function is declared directly on object it wont get converted to method because it was not declared in the class. It is declared on the object
### hence it will stay function

class MyAnotherClass():
    def say_hello(self):    ### At this point this is just a function not method
        print

another_obj = MyAnotherClass()

another_obj.say_hello  ### At this point say_hello is method and is bound to another_obj