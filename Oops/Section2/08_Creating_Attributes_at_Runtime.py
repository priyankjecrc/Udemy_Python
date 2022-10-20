## Understanding  - MethodType

## It explain when a function is declared outside the class and assigned to an object it doesn't gets converted to
## method(because that function is not declared inside the class).
## But there is a way in which I can bind a function (which is created outside the class) to the object. This is done using MethodType

class MyClass():
    language = 'python'

obj = MyClass()
obj.say_hello = lambda : print('Hello World')  ## This say_hello will be a Function not a bound method as it is defined outside class
obj.say_hello() ## Now inside say_hello() we can't do anything with obj because obj was not passed automatically inside say_hello()
                ## unlike the way it happens when we defined say_hello() inside class

obj.say_sth = lambda self:print(self)
obj.say_sth() ## TypeError: <lambda>() missing 1 required positional argument: 'self'
              ## This will throw error. Because it is not a bound method and nothing will be passed to self


## Now the above concern is -> Can we create and bind a method to instance at runtime ??
## YES -> we just to need to define a method that can bind the function to instance. It can be done using MethodType(function, object)

from types import MethodType

newobj = MyClass()
newobj.say_hello = MethodType(lambda self: print(f'Hello {self.language}'), newobj) ## now say_hello() is a method bound to newobj


newobj.say_hello() ## Hello python

## Above line might lead to confusion as how self.language is able to print 'Hello python'. Because newobj must be getting passed
## to self otherwise it won't be able to print 'Hello python'

## say_hello() above is defined as lambda. Below is its equivalent

'''
def say_hello(self):
    print(f'Hello {self.language}')
    
newobj.say_hello = MethodType(say_hello,newobj)  --> now this will bind say_hello to newobj.
                                                     Here MethodType has bound say_hello to newobj, therefore newobj will be
                                                     automatically passed as first argument in say_hello (this is what we discussed in Method in 06_FunctionAttributes.py)   
                                                     This is how self in lambda above was able to do self.language
'''


print(newobj.__dict__)  ## say_hello() not function anymore - it is now bound method for newobj
                        ## {'say_hello': <bound method <lambda> of <__main__.MyClass object at 0x000001EDF19D0F70>>}


print(newobj.say_hello.__self__)  ## <__main__.MyClass object at 0x0000026B3B17AF70>
print(newobj.say_hello.__func__)  ## <function <lambda> at 0x0000026B3AE8DE50>


### Imp - Trying something weird

weirdobj = MyClass()
weirdobj.language = 'java'

weirdobj.say_hello = MethodType(lambda self: print(f'Hello {self.language}'), newobj) ### Binding say_hello to newobj not to weirdobj
weirdobj.say_hello() ### Hello Python is output not Hello Java. Because for weirdobj we binded say_hello to newobj




del newobj

weirdobj.say_hello()  ## Hello python......o/p still Hello Python, but why? We have deleted newobj in line above.
print(newobj)         ## May be because only reference newobj is gone but obj is still there


