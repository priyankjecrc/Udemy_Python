

class Parent():
    def __init__(self,name,age):
        pass

class Student(Parent):
    pass

s1 = Student()  ## Will give error - __init__() missing 2 required positional arguments: 'name' and 'age'