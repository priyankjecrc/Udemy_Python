
## In previous file - 04_a_1_Delegating_to_Parent we mentioned something very imp regarding - super(Student, self).sing()- This also means search for sing() in super class of Student.
## We will explore this point in this file


class TestParent():
    def sing(self):
        print(f'inside TestParent Class and self passed is{self} ')

class TestChild(TestParent):
    def sing(self):
        print('inside TestChild class')

testObj = TestChild()






class Person():


    def __init__(self):
        print('Inside Person Class')
        print(f'Inside Person class and passed object is {self}')

    def sing(self):
        print(self)
        return 'Person is singing'

class Student(Person):

    def __init__(self):
        print('Inside Student Class')

    def sing(self):
       return super(TestChild,testObj).sing()       ## VV.IMP - super(TestChild, testObj).sing()- This also means search for sing() in super class of TestChild.
                                                    ## ie. Search for sing() in TestParent

    pass

s1 = Student()
print(s1.sing())   ## - will go to superclass of TestChild ie into TestParent to find sing()

print(Student.__mro__) ## IMP -  __mro__ method resolution order


