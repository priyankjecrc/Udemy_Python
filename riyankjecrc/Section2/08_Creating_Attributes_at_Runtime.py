## Understanding  - MethodType

## It explain when a function is declared outside the class and assigned to an object it doesn't gets converted to
## method(because that function is not declared inside the class).
## But there is a way in which I can bind a function (which is created outside the class)to the object. This is done using MethodType

class MyClass():
    language = 'python'

obj = MyClass()
obj.say_hello = lambda : print('Hello World')  ## This say_hello will be a function not a bound method as it is defined outside class
obj.say_hello() ## Now inside say_hello() we can't do anything with obj because obj was not passed automatically inside say_hello()
                ## unlike the way it happens when we defined say_hello() inside class

## Now the above concern is -> Can we create and bind a method to instance at runtime ??
## YES -> we just to need to define a method that can bind the function to instance. It can be done using MethodType(function, object)

from types import MethodType

newobj = MyClass()
newobj.say_hello = MethodType(lambda self: print(f'Hello {self.language}'), newobj) ## now say_hello() is a method bound to newobj

newobj.say_hello()

print(newobj.__dict__)  ## say_hello() not function anymore - it is now bound method for newobj
                        ## {'say_hello': <bound method <lambda> of <__main__.MyClass object at 0x000001EDF19D0F70>>}



### Imp - Trying something weird

weirdobj = MyClass()
weirdobj.language = 'java'

weirdobj.say_hello = MethodType(lambda self: print(f'Hello {self.language}'), newobj) ### Binding say_hello to newobj not to weirdobj

weirdobj.say_hello() ### Hello Python is output not Hello Java. Because for weirdobj we binded say_hello to newobj



