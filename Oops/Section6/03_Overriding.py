
class Person():
    def eat(self):
        print(str(self)+ ' eat')

    def sleep(self):
        print(str(self)+ ' sleep')

    def routine(self):
        self.eat()
        self.sleep()



class Student(Person):

    def sleep(self):    ### Just overriding sleep function. Check the results
        print(str(self)+' Inside Student Class'+' sleep')

s1 = Student()
s1.routine()




