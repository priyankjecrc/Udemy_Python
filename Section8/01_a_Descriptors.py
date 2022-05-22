
## https://realpython.com/python-descriptors/ -- Very Very Imp... Go through it
## Lookup chain is very important

class Verbose_attribute():
    def __get__(self, obj, type) -> object:
        print(f"printting self : {self}")
        print(f"printing obj : {obj}")
        print(f"printing type : {type}")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
