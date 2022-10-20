## Abstract CLasses    - From code with Harry.
## Interface - A class with just abstract methods will be called as interface. If we add some function to it which is
## not abstract, the class will be converted to Abstract class
## Multiple Inheritance -

## Example of Abstract Class

from abc import ABCMeta,abstractmethod  ## both are necessary. This is for old python version before 3.4
                                        ## For new python version from abc import ABC, abstractmethod

class Shape(metaclass=ABCMeta):         ## necessary to give.
                                        ## In new python version more that 3.4 we can write class Shape(ABC)

    @abstractmethod                     ## necessary to give
    def printArea(self):
        return 0

class Square(Shape):

    def __init__(self, length):
        self.length = length


    def printArea(self):                 ## Error - Can't instantiate abstract class Square with abstract method printArea
        return self.length*self.length   ## will be thrown if I don't define printArea here


square = Square(100)

calculatedArea = square.printArea()
print(f'Calculated Area of Square is = {calculatedArea}')