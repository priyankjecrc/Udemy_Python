
## Another approach to deal with overriding

class IntegerValue():
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[instance] = value


    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.values.get(instance)



class Point2D():
    x = IntegerValue()
    y = IntegerValue()

p1 = Point2D()
p2 = Point2D()

p1.x = 100
p1.y = 200

p2.x = 500
p2.y = 600

print(Point2D.x.values) ## {<__main__.Point2D object at 0x0000022857FB4FD0>: 100, <__main__.Point2D object at 0x0000022857FB41F0>: 500}

## Problem with this apprach is, if I delete p1 the reference(Strong Reference) will still be there in the dictionary

## Solution is to use weak reference