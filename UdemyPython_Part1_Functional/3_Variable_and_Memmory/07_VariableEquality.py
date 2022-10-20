
## To compare Memmory Address we use 'is' also called as Identity Operator
## To compare internal states of the object we use '==' also called as Equality Operator

a = 10
b = 10.0

print(a is b) ## False..as 2 objects are created and since 10 and 10.0 are of diif types, no shared reference will be created
print(a == b) ## True... Will check on values and values are still equal

c = 'hello'
d = 'hello'

print(c is d) # True, but dont count ot it
print(c == d) # True

## None is also an object. It is an singleton object. Doesn't matters how many None objects you create, all of them will
## point to same one None object
## Python will create shared reference when assigning a variable to None

f = None
g = None

print( f is g) ## True
print(f == g) ## True


