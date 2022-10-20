
## We can't raise any Exception. The raised object must be an instance of BaseException

ex = ValueError('a','b','c')

print(ex.args)  ## ('a', 'b', 'c')
print(str(ex))  ## ('a', 'b', 'c')
print(repr(ex)) ## ValueError('a', 'b', 'c')

try:
    raise ValueError()
except ValueError as ex:
    print('Exception handled')  ## We just want to print or log some message and then wish to continue with the Error
    raise                       ## Just 'raise' is used here. Error will continue as we have raised it






## We know that Stack Trace is created for error, but if we want to show only one particular error in Stack Trace
## then we will use "raise <some error>  from". This way we can hide error

## Example 1:

'''   
## Commenting out because Example 2 will not run otherwise. Uncomment this and run
try:
    raise ValueError()
except:
    try:
        raise TypeError()
    except TypeError as ex:
        raise KeyError() from None    ## We are bypassing Type Error and Value Error and in Stack Trace we will only see Key Error
'''

'''
## Example 2: Uncomment this and run

try:
    raise ValueError()
except ValueError as ex1:
    try:
        raise TypeError()
    except TypeError as ex2:
        raise KeyError() from ex1  ## We are bypassing Type Error, hence in stack trace we will only see Key Error and Value Error
'''