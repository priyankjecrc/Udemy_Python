
def outerFunc():
    x = 100
    def innerFunc():
        nonlocal x   ## IMP - It will only look into Enclosing local scope, here outerFunc gives enclosing local scope
        x = 500
    innerFunc()  ## There is need to call it... otherwise x in outer func will remain 100

    print(x)

outerFunc()    ## 500


y = 1000


def outerFunc1():

    def innerFunc1():
        nonlocal y   ## SyntaxError: no binding for nonlocal 'y' found. Because python will look only into enclosing local scope
        y = 500
    innerFunc1()

    print(y)

outerFunc1()


## Confusing Example

def outer():
    x = 1000
    def inner1():
        nonlocal x
        x = 2000

        def inner2():
            nonlocal x
            x = 3000

        inner2()   ## 1. This will change inner1 x to 3000
        print(x)   ## 3000

    inner1()       ## 2. This will change outer x to 3000
    print(x)       ## 3000


outer()

## Another confusing Example

z = 1000

def firstFunc():
    global z
    z = 1000           ## Z is not local, it is global

    def secondFunc():
        nonlocal z      ## SyntaxError: no binding for nonlocal 'z' found, because of reason listed above
        z = 2000

    secondFunc()
    print(z)

firstFunc()