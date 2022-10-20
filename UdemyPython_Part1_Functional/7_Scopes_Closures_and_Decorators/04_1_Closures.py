
## https://www.youtube.com/watch?v=tNSOaA1z6Uo .... watch this video after completing below part

## Lambda are not closure
## Clousre is created when Function is created
## Free variable - Variables that are used in a Function, which are neither Local variable nor parameters of that Function

## Eg - of Free Variable

def outsideFunc():
    k = 0
    def innerFunc(l):  ## l is not a Free variable
        m = 0         ## m is not a Free variable
        print(k)     ## k inside innerFunc is Free variable because it is not local variable nor parameter of innerFunc



## CRITERIA for creating a CLOSURE -

## 1. We must have a nested function (function inside a function).
## 2. The nested function must refer to a value defined in the enclosing function.
## 3. The enclosing function must return the nested function.


## What are closure

def outerFunc():
    x = 'python'

    def innerFunc():
        print(x)      ## Since x is SHARED variable between 2 SCOPES, python will create a CLOSURE.
                      ## Since there is no assignment to x, therefore it is NOT a local variable
    return innerFunc  ## We are not calling innerFunc, because calling would be innerFunc(). We are just returning innerFunc

fn = outerFunc()


fn()  ## python  .... Problem ? - innerFunc still have access to 'x' even though outerFunc has finished running. Its scope is gone
      ## so how can fn() now go and see 'x' in outerFunc. outerFunc had finished running before we called fn
      ## This is possible because of Closure. So when outerFunc has already finished running Closure still has 'x'


## So how Closure is achieved - ?... It is achieved by creating an intermediary cell(actually an object). Now this cell will contain reference to another object
## and that another object is 'python'

##  x of outerFunc -> cell -> 'python'
##  x in innerFunc -> cell(same as above) -> 'python' (same as above)... Actually x of outerFunc() and innerFunc() are same. Its just that they are in diff scopes

## IMPORTANT ....

## Now when outerFunc has finished running and its scope is gone. But x will still be there, because there is still reference to it from innerfunc.
## x of innerfunc is still pointing to cell.
## And because cell still has reference, it is not garbage collected. Hence x in innerFunc will still have access to 'python' through cell



print(fn.__code__.co_freevars)  ## ('x',)
print(fn.__closure__)  # (<cell at 0x00000253EBAB0FD0: str object at 0x00000253EB7F9FB0>,) -- make note of  1. cell and 2. object that we talked about above


## Multiple Instances of Closure

def counter():
    count = 0

    def inc():
        nonlocal count    ## If I comment this line out than error will be shown in line count = count+1,
        count = count+1   ## because than count will be considered as a local variable... Error - .. local variable 'count' referenced before assignment
        return count
    return inc

f1 = counter() ## Closure will be created
f2 = counter() ## Another Closure will be created and will be different from one created above

print(f1.__closure__) ## (<cell at 0x00000268F77CAA38: int object at 0x00007FFCC649A180>,)
print(f2.__closure__) ## (<cell at 0x00000268F9509C78: int object at 0x00007FFCC649A180>,)


print(f1(),f1(),f1())  ## 1 2 3  ... remember we are not calling counter again and again, we are calling inc() again and again
print(f2(),f2(),f2())  ## 1 2 3 ... My Concern - f1() is actually calling inc().. Now once inc() is called it should go outof scope
                       ## If it goes out of scope than access to count should not be available but it is available. So when f1()
                       ## was called second time, it must give error or something but it's not. It may be because closure is always
                       ## attached to inc()..but this is just a guess.


## Sharing Extended Scope

def outer():
    count = 0

    def inc1():
        nonlocal count
        count = count+1
        return count

    def inc2():
        nonlocal count
        count = count+1
        return count

    return inc1, inc2

f1,f2 = outer()
print(f1())  ## 1
print(f2())  ## 2 - IMP - have a look at this
print(f1.__closure__)   ## (<cell at 0x0000020D026889A8: int object at 0x00007FFCD60CA1C0>,)
print(f2.__closure__)   ## (<cell at 0x0000020D026889A8: int object at 0x00007FFCD60CA1C0>,)
                        ## Both the cell are same.
                        ## So there are 2 different closure sharing the same cell


## IMP - A very confusing example and Common Mistake

adders = []

for n in range(1,4):
    adders.append(lambda x:x+n)  ## Imp - We are not calling Lambda, we are just defining lambda here

print(adders[0](10))  ## 13    ... Here we are actually calling Lambda
print(adders[1](10))  ## 13
print(adders[2](10))  ## 13 .... All of them 13.. we were expecting 11, 12, 13...What happened ?
                      ## This happened because n is not local to Lambda, it is defined in outer scope and it is accessed when Lambda is called not when it was defined
                      ## So when Lambda was called value of 'n' was = 3. Therefore we got this result



## IMP - Solution of above problem

adders1 = []

for n in range(1,4):
    adders1.append(lambda x,y = n : x + y) ## We are assignning default value to y, and instead of n we will be adding y.
                                           ## Now remember when the default values are evaluated at function definition time only.
                                           ## So everytime lambda is accessed(means defined here) y will have current value of n
                                           ## so basically it will be  - lambda x,y = 1 : x + y, lambda x,y = 2 : x + y, lambda x,y = 3 : x + y



print(adders1[0](10)) ## 11
print(adders1[1](10)) ## 12
print(adders1[2](10)) ## 13


## One Confusing Case

def counter1():
    count = []

    def inc():
        nonlocal count
        count.append(1)
        return count
    return inc



myfunc = counter1()
myfunc1 = counter1()

print(myfunc1(),myfunc1(),myfunc1())  ## [1, 1, 1] [1, 1, 1] [1, 1, 1] ... Why ?
                                      ## Because printing will happen at once..finally count in myfunc1() will be [1,1,1]

print(myfunc1()) ## [1, 1, 1, 1] ... because after execution of above print count in myfunc1() was [1,1,1]
print(myfunc1()) ## [1, 1, 1, 1, 1]
print(myfunc1()) ## [1, 1, 1, 1, 1, 1] .... Ok..No prob so far






