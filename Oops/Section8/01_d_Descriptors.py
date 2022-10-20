## Trying to handle old problem of overriding

class IntegerValue():

    def __init__(self, Passvalue):
        print('inside init')
        ## self.givenvalue = Passvalue  ## This will create problem   ------ 1
        self.givenvalue = '_'+ Passvalue ## Will assign Passvalue(which will be x and y) to instance x and y


    def __set__(self, instance, value):            ## Will create attribute _x and _y on p1 and p2
        setattr(instance,self.givenvalue, value)  ## if I use ---- 1 then it will be like
                                                  ## setattr(p1,x,100)... like p1.x = 100..p1.x is getting called again
                                                  ## .. this will cause infinite loop because it will call p1.x again

## Issue is coming because we are calling p1.x. If we do something like instance.__dict__[self.givenvalue] = value..
## it will be like instance.__dict__[x] = 100 and this will work because we are no more calling p1.x


    def __get__(self, instance, owner):
        return getattr(instance,self.givenvalue, None)

class Point2D():
    x = IntegerValue('x')   ## check here.. we have passed 'x' and 'y' as parameters
    y = IntegerValue('y')

p1 = Point2D()
p2 = Point2D()

p1.x = 100
p1.y = 200

print(p1.__dict__)  ## {'_x': 100, '_y': 200}

p2.x = 300
p2.y = 300

print(p1.__dict__)  ### {'_x': 100, '_y': 200}
print(p2.__dict__) ### {'_x': 300, '_y': 300}

## Overriding issue gets solved here
## Drawbacks -  1. x = IntegerValue('x') -- specifying 'x' as parameter. This can be handled by __set_name__ method.. explained later in SetNameMethod.py
## 2. if I do something like p1._x = '5000' then it will be problem as somebody can use _x as attribute

p1._x = 5000
print(p1.__dict__) ## {'_x': 5000, '_y': 200} while originally it was {'_x': 100, '_y': 200}