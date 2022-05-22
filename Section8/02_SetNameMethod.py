
## The problem we mentioned in 01_d_Descriptors.py about specifying x in parameter, can be solved by __set_name__

## Look at look up chain explanation on https://realpython.com/python-descriptors/

class IntegerValue():

    def __set_name__(self, owner, name):
        print(name)                        ## Here value of name will be x . This can be utilized to solve problem we faced as mentioned above
        pass

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass

class Point1D():
    x = IntegerValue()  ## x will be O/P
