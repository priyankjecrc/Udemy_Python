
## Watch video no 76 and 77 - Parameters Default Beaware


## When a Module is loaded, all the code gets executed immediately.

## Very IMP Lesson--- Never use Mutable default types in the function parameters.. But there can be use case for this situation...
## Go through video 77 @ 12 min


def my_func(someval,someList = []):  ## here Default Parameter value is evaluated only once when the function is defined, not each time the function is called
     print(someList)              ## now when we call my_func multiple times, we are not passing anyvalue for somelist. Hence someList will still be
     someList.append(someval)        ## pointing to same old object(or memmory location). This problem will not happen in case of Immutable because
     print(someList)               ## any changes made in immutables will lead to creation of new object


list1 = [1,2,3]
list2 = [4,5,6]

my_func(list1) ## []
               ## [[1, 2, 3]]


my_func(list2)  ## [[1, 2, 3]]             ## Strange behaviour... happened because of reason listed above
                ## [[1, 2, 3], [4, 5, 6]]

## Solution

def my_func(someval,someList = None):
    if someList == None:           ## New addition to solve above problem
        someList = []
    print(someList)
    someList.append(someval)
    print(someList)

my_func(list1)  ## []
                ## [[1, 2, 3]]

my_func(list2)  ## []
                ## [[4, 5, 6]]

### Writing a Factorial program to demonstrate use case of using default mutables.. Exploring some issues with print('dfdfd') and return fact

def calcFact(n):
    if n<=1:
        return n
    else:
        print(f'Calculating Factorial for {n}')
        fact = n*calcFact(n-1)
        print('dfdfd')              ## Have a look at output and find why this is getting repeated..
        return fact

calcFact(4)     ## Calculating Factorial for 4
                ## Calculating Factorial for 3
                ## Calculating Factorial for 2
                ## dfdfd
                ## dfdfd
                ## dfdfd

## calcFact(4) is giving some strange output...like dfdfd multiple times





## calcfact(4) -  decoding why 'dfdfd' will be repeated

## fact = 4 * calfact(3)
## fact = 4 * (fact = 3 * calfact(2))
## fact = 4 * (fact = 3 * (fact = 2 * calfact(1)))
## fact = 4 * (fact = 3 * (fact = 2 * 1))

## now calfact pertaining to (fact = 2 * 1) will complete its execution ie 1. print('dfdfd') and then 2. return fact will be executed
## .. Likewise calfact will be completely executed multiple times. Therefore 'dfdfd' will be printed multiple times


## In above calcFact(4) we saw that it was printing Calculating Factorial multiple times... It is not required.
## See below approach to handle this situation


def calcFactCache(n, resultCache = {}):
    if n<=1:
        return n
    elif n in resultCache:
        return resultCache[n]
    else:
        print(f'Calculating Factorial for {n}')
        fact = n*calcFactCache(n-1)
        resultCache[n] = fact
        return fact

print(calcFactCache(4))  ## Calculating Factorial for 4
                         ## Calculating Factorial for 3
                         ## Calculating Factorial for 2
                         ## 24

print(calcFactCache(5))  ## Calculating Factorial for 5
                         ## 120                          ## See the difference here from above



def testdunc(someval,passval = []):
    passval.append(20)
    print(passval)

testdunc(10)
testdunc(20)