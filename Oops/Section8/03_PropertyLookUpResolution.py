
## Data Descriptors - If descriptors define __set__ or __del__ or both
## Non Data Descriptors - If descriptors define only __get__

## .__set_name__() this will not matter

## Resolution order rule 1 - If descriptor is Data Descriptors - will look into __get__.
##                                                               If __get__ is not present than it will look into __dict__

class MyClass1():   ## This is Data Descriptor

    def __set__(self, instance, value):
        pass

    '''
    def __get__(self, instance, owner):                ## First s1.x1 will look into __get__. Since here __get__ is absent,
        return 'inside __get__ of Data Descriptor '    ## therefore it will look into dict
    '''

class Student1():
    x1 = MyClass1()


s1 = Student1()

s1.__dict__['x1'] = 'looking into dict of Data Descriptor'

print(s1.x1)
print(s1.__dict__)


##########################################################
##########################################################


## Resolution order rule 2 - If descriptor is Non Data Descriptor, s2.x2 will look into __dict__ first. If it doesn't find there
##                           then it will look into __get__

class MyClass2():  ## This is NonData Descriptor

    def __get__(self, instance, owner):
        return 'inside __get__ of Non Data Descriptor'

class Student2():
    x2 = MyClass2()

s2 = Student2()

s2.__dict__['x2'] = 'looking into dict of Non Data Descriptor'

print(s2.x2) ### looking into dict of Non Data Descriptor

