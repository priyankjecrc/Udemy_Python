## It is a good practise to always use super first but why?? it is shown below

### Imp -
class Person():
    def details(self, name, age):
        self.name = name
        self.age = age
        self.city = 'N/A'

class Student(Person):
    def details(self, name, age, city):
        self.city  = city
        super().details(name, age)  ## We are calling super after self.city = city. This might create problems as explained below

    def printDetails(self):
        print(self.name,self.age,self.city)
        print(super())  ## <super: <class 'Student'>, <Student object>> - A temporary object of Parent class returned by super()
                        ## and that's how we are able to access functions and attributes defined in Parent class

s1 = Student()
s1.details('pinkoo',33,'agra') ## Our expectation is name = pinkoo, age = 33, city = agra
s1.printDetails()  ## but O/P we get is pinkoo 33 N/A... Why N/A... because we called super().details(name, age) after self.city = city.
                   ## value set by self.city = city ie(agra) will be overridden by super().details(name, age)

## Also watch Delegating to parent - coding video. A imp situaton is explained after half of the video