

## Why use Named Tuple - Tuples are immutable, whether named or not. Namedtuple only makes the access more convenient,
## by using names instead of indices.

## Named Tuple - they are subclasses of Tuple(hence they will also be immutable). They add a layer of property names to the positional elements
## Named Tuple is a function, which generates new class. It is a class factory

## Named Tuple need following things to create a class
#   1. The class name we want to use
#   2. A sequence of field names(strings) we want to assign in the order of the elements in tuple. Field names cannot start with underscore
#   3. The return value of call to the Named Tuple will be a class
#   4. We need to assign that class to a variable name in our code so we can use it to construct instances

from collections import namedtuple

point2d = namedtuple('Point2D', ['x','y']) ## This will return a class and assign to point2d not 'Point2D'
## point2d = namedtuple('Point2D', 'x y') ## Can also be created in this way

pt1 = point2d(10,20) ## generating instances to class point2d
pt2 = point2d(x = 30, y = 40 )
pt3 = point2d(10,20)

x1,y1 = pt1 ## unpacking

for e in pt1:  ## iterating a tuple. We can also slice a tuple
    print(e)

#======================== All Imp points below ================================

print(pt1) ## Point2D(x=10, y=20)
print(isinstance(pt1, tuple)) ## True
print(pt1 is pt3) ## False
print(pt1 == pt3) ## True
print(max(pt1)) ## 20
print(pt1._fields)  ## ('x', 'y')
# print(pt1._source) ## ._source has been removed in python 3.7

print(pt1._asdict()) ## OrderedDict([('x', 10), ('y', 20)]) .. An ordered dictionary. Can be converted into dict
                     ## why OrderedDict?... because order is imp in tuples

pointDict = pt1._asdict()
print(pointDict['x'])  ## 10


## pt1.x = 100  ## AttributeError: can't set attribute, because tuples are immutable



