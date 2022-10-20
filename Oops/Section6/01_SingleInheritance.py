## Read about Composition and Inheritance --- https://realpython.com/inheritance-composition-python/
## Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes.
## isinstance() and issubclass()

## Prefer to use isinstance() instead of type() because isinstance() takes care of inheritance but type() doesn't

## issubclass() looks for relationship between classes not instances

## Have a look into this relationship  Person <-- Student <-- CollegeStudent
## Person is parent of Student
## Person is not parent of CollegeStudent. Parent is a direct relationship
## subclass is not necessarily direct... issubclass(Student,Person) => True
##                                       issubclass(CollegeStudent,Person) => True
## issubclass(Student,Student) => True

## IMP -
## cls1 = Student
## cls2 = Student....  issubclass(cls1,cls2) => True... cls1 and cls2 are not objects

## Every class that you create in Python will implicitly derive from object.
## The exception to this rule are classes used to indicate errors by raising an exception.