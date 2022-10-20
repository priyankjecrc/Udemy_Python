## We can't modify a tuple as they are immutable. If we make some change new object will be created
## ._replace - To replace some value with new one in tuple
##


from collections import namedtuple

Point2D = namedtuple('Point2D', ['x','y'])

pt1 = Point2D(10,20)

## Now we want to change value of x. It can be done using _replace

pt1 = pt1._replace(x = 100) ## We have to use key word arguments, for eg: we have used x here

print(pt1)

## WE want to add one more field

totalField = Point2D._fields+('z',)

Point2D = namedtuple('Point2D', totalField)