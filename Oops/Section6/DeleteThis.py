
class Person():
    def printName(self):
        print('inside Person Class')
        print(self)

class Student(Person):
    def printName(self):
        print('inside Student Class')
        super(Student,self).printName()

class me(Student):
    def printDetails(self):
        ##super().printName()
        super(dropThis,self).printName()

class dropThat():
    def printName(self):
        print('inside drop that')

class dropThis(dropThat):
    def printName(self):
        print('inside drop this')

s1 = me()
dt = dropThis()


me.printDetails(dt)

