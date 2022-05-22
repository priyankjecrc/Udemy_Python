
## When we use or invoke a function in Python, we typically say that we call the particular function.
## The “calling” is achieved by placing a pair of parentheses following the function name,
## and some people refer to the parentheses as the call operator. Without the parentheses, Python interpreter
## will just generate a prompt about the function as an object itself — the function doesn’t get called.

## Classes are callable because when we use MyClass() with parenthesis object will get return

## Python has a built-in function callable, which allows us to determine if an object is callable or not.

class MyClass():
    pass

print(callable(MyClass)) ## Class is callable

obj = MyClass()
print(callable(obj)) ## This object is not callable as we have not implemented __Call__ method  inside class

class TestClass():
    def __call__(self, *args, **kwargs):
        pass

testObj = TestClass()
print(callable(testObj)) ## True as we have defined __call__ inside the class TestClass

def sayHello():
    pass

print(callable(sayHello)) ## True