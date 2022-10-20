### When we create a class python automatically adds behaviour to class
### It also adds something that makes class callable
### The return value of that callable is object

### Objects can also be make callable by implementing .__call__ method
### Imp -> Python implements .__call__ method automatically when we create a class. This makes class callable
### and the return value of this callable will be object whose type will be class that we created
### This class instance object will have its own name space and it will be distinct from the name space of class
### This object will have some attributes that Python automatically implements for us for eg - __dict__, __class__

class MyClass():
    print('my class')


obj = MyClass()  ## will print - my class, because of the print statement that we gave in class

print(MyClass.__dict__) ## will not be empty
print(obj.__dict__) ## will be empty. This shows that the class and its object have different namespace
print(obj.__class__) ## <class '__main__.MyClass'>

## to check type of class we must use type

class TestClass():
    __class__ = str

p = TestClass()

print(p.__class__, type(p)) ### <class 'str'> <class '__main__.TestClass'>. Here we messed with __class__ property therefore
                            ### results are confusing.. Therefore we must use type(p) as it figures out the class from which object
                            ### is created


### Not important right now
print(isinstance(p, TestClass)) ### True
print(isinstance(p,str))        ### True but why ?. This will be discussed in metaprogramming
