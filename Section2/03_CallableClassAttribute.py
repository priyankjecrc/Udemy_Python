### Attributes value can be any object.
### -> They can be other class
### -> They can be any callable
### -> They can be anything

class MyClass():
    language = 'python'

    def say_hello():      ### -> say_hello() is an attribute of class MyClass()
        print('hello world')  ### say_hello() is going to be callable whose type is going to be a Function



print(MyClass.__dict__)       ### say_hello': <function MyClass.say_hello at 0x000001EBE408CDC0>

### Ways of calling

### Method 1
print(MyClass.__dict__['say_hello'])  ### <function MyClass.say_hello at 0x00000272ECACCDC0>
MyClass.__dict__['say_hello']()

### Method 2

getattr(MyClass,'say_hello')()

### Method 3

MyClass.say_hello()