
## To be done after completing decorators topic




def inside_outer_func():
    print('inside outer func')

def outer_Func(passFunc):
    print('inside outer func')
    passFunc()
    return inside_outer_func


def inner_func():
    print('inner func')


inner_func = outer_Func(inner_func) ## Function is passed inside other function and a function is returned. This returned function is
                                   ## reassigned to the function which was passed
                                   ## we will add @outer_Func before def inner_func()
                                   ## after that we wont need this line - inner_func = outer_Func(inner_func)

inner_func()