## Every object in python has associated Boolean value
## Any Non Zero Number -> True
## 0 -> False
## Emplty Collection where len() gives 0 -> False

## By default any object also has true value and it can be overridden by defining __bool__ method

## If __bool__ is not defined than Python looks for __len__ method in a class
## If neither __bool__ or __len__ is present than it will be consider as True
## When both .__bool__() and .__len__() are defined, .__bool__() takes precedence:

## Read - https://realpython.com/python-boolean/


## IMP -
## AND operator - if first input is False, second input will not be evaluated and result will be false.
## This could create a problem as shown below

print(False and 1/0) ## O/P is False, This should raise exception as 1 is divided by 0, but as first input is False
                     ## second input will not be evaluated

## print(1/0)  ## Exception occurred

## IMP -
## OR operator - If first input is True, second input will not be evaluated and result will be True

## The singleton object None is always false


## If __bool__ is not defined than Python looks for __len__ method in a class or object or function
## If neither __bool__ or __len__ is present than it will be consider as True

def checkBool():
    pass

print(bool(checkBool())) ## with brackets - Will give False as checkBool is not returning anything
print(bool(checkBool))  ## without brackets - Will give true

print(any([0,1])) ## True...any() checks whether any of its arguments are truthy:

