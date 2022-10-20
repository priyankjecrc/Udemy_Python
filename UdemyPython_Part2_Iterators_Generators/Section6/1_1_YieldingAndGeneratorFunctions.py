
## https://python-course.eu/advanced-python/generators-and-iterators.php

## Why we wish to use Generators - If we wish a FUNCTION to behave like an iterator, then we will use generators
## Actually generators are Iterators.. they have __next__ and __iter__ ...

## Since iterators can be iterated only once likewise Generators can also be iterated only once

## To make above statement possible, python uses YIELD keyword
## Use of Yield
## 1. It emits a value
## 2. When Yield is encountered, the Function is suspended but it retains its current state
## 3. Calling next on the function will resume function running process, and whatever follows after Yield statement will be run
## 4. If function returns something, - StopIteration exception will occur

## Everyfunction returns something.. If we don't have return statement, it will return none





def song():
    print('This is my song1')
    yield 'I am good anf this is my kungfu'  ## Whenever there is yield in function, python will understand that it is a generator


    print('This is my song2')
    yield 'I sllep in night and work in day'

                          ## IMP
mysong1 = song()          ## When song() is encountered, function will not be run. song() will only return generator object. This happens because
                          ## song() contains 'yield'

line1 = next(mysong1)     ## This is my song1 ... next(mysong1) will return value of first 'yield'. And the execution of function body is paused.
                          ## now 'line' will hold the value that was emitted by first 'Yield'

print(line1)              ## I am good anf this is my kungfu


line2 = next(mysong1)     ## This is my song2 .. This will start execution of function again from its last 'yield'
print(line2)              ## I sllep in night and work in day


##line3 = next(mysong1)    ## StopIteration exception


print(mysong1) ## <generator object song1 at 0x00000295ED744A48>



## ==================================================================================================================================== ##


## Can we use for loop over Generators - yes. (as we know for calls next(), same kind of deal is here)

mysong2 = song()

for i in mysong2:         ## StopIteration will not be raised as For loop understand StopIteration exception
    print(i)

## This is my song1
## I am good anf this is my kungfu
## This is my song2
## I sllep in night and work in day



## ==================================================================================================================================== ##

## Another Example.. we have used return statement here

def habit():
    print('This is my habit1')
    yield 'I sleep late in night'  ## Whenever there is yield in function, python will understand that it is a generator

    print('This is my habit2')
    yield 'I eat too much'
    return 'We are in the return statement'


myhabit1 = habit()

habit1 = next(myhabit1)  ## This is my habit1
print(habit1)           ## I sleep late in night

habit2 = next(myhabit1)  ## This is my habit2
print(habit2)           ## I eat too much

## habit3 = next(myhabit1)  ## StopIteration: We are in the return statement
                        ## 'We are in the return statement' is the return value we mentioned in return statement



## ==================================================================================================================================== ##

## Using For loop

myhabit2 = habit()

for i in myhabit2:           ## As we can see here that return statement of habit() doesn't gets printed
    print(i)

## This is my habit1
## I sleep late in night
## This is my habit2
## I eat too much
