
## IMP --- for loop

for i in range(10):
    x = 2*i

print(i,x)  ## 9,18 - In other language like java it will not work because scope of x and i will be in for loop.
            ## but in python its not like that.



## IMP - When we use a Global Keyword, the variable does not have to exist

def myfunc():
    global a   ## a is not existing before
    a = 100

## print(a)    ## Error: and it is expected as we haven't define a

myfunc()

print(a) ## 100... but why..?
         ## we called myfunc(). In this function we created a variable in Global scope and assigned value to it


## IMP -----

b = 200

def testFunc():
    print(b)
    b = 500    ## As soon as python see this during compile time, python will say that b is local variable(because 500 is assigned to b)
    print(b)   ## and not Global Variable. The first line says print(b), therefore it will look for 'b' in local scope and will not find it.
               ## and this will give error

testFunc()  ## UnboundLocalError: local variable 'b' referenced before assignment... but why ?. See explanation above


## Compare following testFunc1() with above testFunc()

d = 200

def testFunc1():
    print(d)     ## No redline as above once we have commented the line below
##    d = 500    ## As soon as python see this during compile time, python will say that b is local variable(because 500 is assigned to b)
    print(d)

testFunc1()  ## No error