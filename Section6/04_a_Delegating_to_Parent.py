
## IMP - https://realpython.com/python-super/
## super() method allows us to reference parent class
## eg - super().method(). Though we are calling method() present in parent but method() will still be bound to instance


class Person():

    def sing(self):
        print(self)
        return 'Person is singing'

class Student(Person):
    def sing(self):
       return super().sing() ## -> can be decoded to return super(Student, self).sing(). self will be s1
                             ## A temporary object of Parent class Person will be super() and that's how we will access sing() function of parent
                             ## sing() will be bound to instance of Student which is s1 (because self is s1)
                             ## proof - <__main__.Student object at 0x000001E5CEFC0FA0> ... printed in sing() method in Person class
                             ## if by mistake i write self.sing() here that it will go into infinite loop

                             ## super() doesn’t return a method. It returns a proxy object.
                             ## This is an object that delegates calls to the correct class methods without making an additional object
                             ## in order to do so.

    pass

s1 = Student()
print(s1.sing())
print(Student.__mro__) ## IMP -  __mro__ method resolution order



