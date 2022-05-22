
class IntegerValue():

    def __set__(self, instance, value):
        instance.value  = value


    def __get__(self, instance, owner):
         return instance.value

class Point1D():
    x = IntegerValue()

p1,p2 = Point1D(), Point1D()

p1.x = 100
p2.x = 200

print(p1.__dict__) ## {'value': 100}
print(p2.__dict__) ## {'value': 200}

## So far no problem

## Introducing Problem

class Point2D():
    y = IntegerValue()
    z = IntegerValue()

p3 = Point2D()

p3.y = 100
p3.z = 200

print(p3.y)  ## 200... We set that as 100 but O/P is 200
print(p3.__dict__) ## {'value': 200} -> no presence of 100
                   ## This happens because value attribute belongs to p3 and it got overridden when we did p3.z = 200