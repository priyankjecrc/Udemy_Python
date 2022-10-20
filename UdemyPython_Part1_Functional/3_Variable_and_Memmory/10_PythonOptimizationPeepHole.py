
## There is another variety of Optimization that happens at 'Compile Time'

## Python code gets compiled when it is run, but it doesn't have to recompile this code everytime when we re-run.
## so certain things get optimized eg - Constant Expressions, Short Sequences of length < 20,

## eg - IMP

24*60 ## This will not get compiled every time. Python will convert this to 1440

## Membership Tests: Mutables gets replaced by Immutables.
## Lists gets converted into Tuples
## Sets gets converted into Frozen Sets

e = 2
if e in [1,2,3]:  ## For optimization [1,2,3] will be converted to tuples - (1,2,3). because Python know [1,2,3] not gonna change
    print('Found the element')

def my_func():
    a = 24*60
    b = [1,2,3]
print(my_func.__code__.co_consts) ## (None, 1440, (1, 2, 3)) - Check 1440 in place of 24*60 and (1,2,3) in place of [1,2,3]