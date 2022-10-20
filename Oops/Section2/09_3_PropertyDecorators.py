## Go through it - Imp point

## Properties are actually descriptors
## Some reference of Section 8 03_PropertyLookUpResolution.py has been used

class MyClass():

    def __init__(self,value):
        self._name = value

    @property
    def name(self):
        return f'inside name and passed name is {self._name}'

    @name.setter
    def name(self,value):
        self._name = value


s1 = MyClass('Priyank')
print(s1.name)               ### inside name and passed name is Priyank
s1.name = 'mummy'
print(s1.name)              ### inside name and passed name is mummy

s1.__dict__['name'] = 'Some other name'  ### inside __dict__ we have added a variable name and have set it's value to = 'Some other name'
print(s1.name)                           ### inside name and passed name is mummy. Still mummy is getting printed
print(s1.__dict__)                       ### {'_name': 'mummy', 'name': 'Some other name'}


## Now according to Descriptor look up resolution if descriptor is Non Data Descriptor, than first we look into __dict__ and if we don't
## find it there than we look into __get__

## Trying to create a class of Non Data Descriptor nature

class Person():  ## Looks like it is Non Data Descriptor

    @property
    def name(self):                       ### Actually it behaves like __get__
        return 'inside name function'

student = Person()

print(student.name)  ## inside name function
print(student.__dict__) ## {}

student.__dict__['name'] = 'Bad student'
print(student.name)   ## inside name function.
                      ## IT looks like it is Non Data descriptor. As per look up resolution for student.name first we should look into __dict__
                      ## But here it looks like it is not looking into __dict__ but it is looking into __get__... WHY ??
                      ## Because here may be we have only defined getter but internally @properties has both __set__ and __del__
                      ## Therefore it is not a Non Data Descriptor





