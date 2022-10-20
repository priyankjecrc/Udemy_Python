
## We can use * and ** for unpacking
## * can be used in LHS and RHS.. ** Can only be used in RHS

print([1,2,3,4,5,6])     ## [1, 2, 3, 4, 5, 6]
print( *[1,2,3,4,5,6] )  ## 1 2 3 4 5 6 ..... unpacked the list


l = [0,1,2,3,4,5,6]

a, *b = l  ## a will take 1st element, b will take all elements after first element
print(a, b) ## 0 [1, 2, 3, 4, 5, 6] - Output is in list format

a, *b, c = l
print(a, b, c) ## 0 [1, 2, 3, 4, 5] 6

a, *b, c = 'priyank'
print(a, b, c) ## p ['r', 'i', 'y', 'a', 'n'] k

## a, *b, *c -> this will not work


l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10]
l3 = 'XYZ'

mergeList = [*l1,*l2, *l3]
print(mergeList) ## [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'X', 'Y', 'Z']

## We can use * in sets as well but order is not guaranteed

## * on dictionaries

d1 = {'p':1,'k':2}
d2 = {'t':3, 'r':5}
d3 = {'z':6,'f':9}

d = [*d1,*d2,*d3]
print(d)  ## ['p', 'k', 't', 'r', 'z', 'f'] - only keys

## We can also do aomething like below, but order is not guaranteed

d3 = {'t':3, 'r':5,'g':10, 'a': 15}

a,*b,c = d3
print(a,b,c) ## t ['r', 'g'] a - order is not guaranteed


## Now how to unpack Key value pairs... use **

d = {**d1,**d2,**d3}
print(d)             ## {'p': 1, 'k': 2, 't': 3, 'r': 5, 'g': 10, 'a': 15}


## One other case

l = [1,2,[3,4]]

a,b,(c,d) = l

print(a,b,c,d)  ## 1 2 3 4

##
l = [1,2,3,'XYZ']

a,*b,(c,d,e) = l

print(a,b,c,d,e) ## 1 [2, 3] X Y Z

## Unpacking in a function

def my_func(a,b,*c):
    pass

my_func(10,20,30,40,50,60) ##  a = 10, b = 20, c = (30,40,50,60) --> IMP mark the difference here... c is Tuple not a list
my_func(*[10,20,30,40,50]) ## check how we unpack list before passing using *. Without * this will not work


def my_func(a,b,*c,d):  ## Will give error as we can't give 'd' without * .. We have to declare d forcibly while calling function
    pass

my_func(10,20,30,40,50,60,70,80) ## This will give error.... We are not forcibly declaring d while calling function

### BUT

my_func(10,20,30,40,50,60,70,d = 80) ## This will work. We are forcing declaring d while calling function
my_func(10,20,d = 100 ) ## ## This will also work...c will be empty Tuple
my_func(d = 100) ## This will not work.. it will ask for a and b


### Using **.. No parameter can come after **kwargs.. ** will be storing values as dictionaries

def my_func(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

my_func(10,20,30,40,50,60, k = 100, c = 200) ## 10 20 (30, 40, 50, 60) {'k': 100, 'c': 200} - check the dict in end

my_func(10,20,30,40,50,60, a = 100, b = 200) ## error as 'a' and 'b' will be having multiple values...because we have a,b
                                             ## in my_func() as well.

