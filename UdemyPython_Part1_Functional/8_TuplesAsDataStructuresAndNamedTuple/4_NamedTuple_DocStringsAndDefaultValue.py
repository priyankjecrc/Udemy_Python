
## Overriding doc String
## Default values

import collections

Point2D = collections.namedtuple('Pointer2D', 'x y')

print(Point2D.__doc__)   ## Pointer2D(x, y)
print(Point2D.x.__doc__) ## Alias for field number 0
print(Point2D.y.__doc__) ## Alias for field number 1

## Overriding doc string

Point2D.__doc__ = '2 Dimensional point Class'

## Setting Default Values

## Method 1 - By Providing defaults to first object, and then using this first object to create new instance

pt1 = Point2D(x = 0, y = 0)

pt2 = pt1._replace(x = 100, y = 100) ## As tuple are immutable, and we are updating its values. This will lead to creation of new instance



## Method 2 - By using __defaults__.. Better method

Point2D = collections.namedtuple('Pointer2D', 'x y z')

Point2D.__new__.__defaults__ = (0,0) ## It assigns from Right to left... From Right first 0 goes to z, second 0 goes to y
                                     ## Remember here we have used Point2D itself not some instance

pt3 = Point2D(10)
print(pt3)  ## Pointer2D(x=10, y=0, z=0)


