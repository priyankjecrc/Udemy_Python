
### Class are also called as types
### Class has state and behaviour for eg - if My_Car is an object than ferrari will be state and acceleration will be behaviour
### Class is also an object
### Class gets created from type metaclass
### Classes are callable - MyClass() - this will return object of MyClass
### Imp  - MyClass is a class but also an object of type - type
###        MyClass() will return an object but its type will be  - MyClass


class MyClass():
    print('inside MyClass')

my_Instance = MyClass()

print(type(MyClass)) ### <class 'type'> ... will return object of type -> type not string 'type'
print(type(my_Instance))  ### <class '__main__.MyClass'> ....this will give MyClass object not string 'MyClass'
print(isinstance(my_Instance,MyClass)) ## True


print(MyClass.__name__) ### MyClass ... This is state provided by default
MyClass() ### The class is callable. This is called as behaviour and is provided by default




