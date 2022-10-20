## Create a new class that inherits from Exception or one of its Subclass
## But most of the times we will inherit from Exception
## Exceptions are classes. We can do all the things that can be done in a class

class AgeLimit50(Exception):
    """ Passed age should be 50 """


class ageClass():

    def __init__(self,passage):
        self.age = passage

    def checkAge(self):
        if(self.age != 50):
            raise AgeLimit50('Passed age is not fifty')


age1 = ageClass(44)
## age1.checkAge()

age2 = ageClass(50)
age2.checkAge()


ex = Exception()
print(repr(ex))