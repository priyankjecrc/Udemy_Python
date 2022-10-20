
## Function are instances of function class
## Class are instance of class type
## Type is an instance of type

## Since all of them are object it means they will also have memory address
## Likewise funciton will also have a memory address
## As any object 1. can be assigned to a variable, 2. Can be passed to a function, 3. Can be returned from a function
## likewise function can also be assigned to a variable, it can also be passed to a function(eg - Decorators), it can also be returned from a function


def my_func():
    pass

print(hex(id(my_func)))  ## 0x21542c4eb80

