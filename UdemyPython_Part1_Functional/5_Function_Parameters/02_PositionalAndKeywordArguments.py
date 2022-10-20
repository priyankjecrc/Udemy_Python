
## Providing default value to parameters

def my_func(a, b = 100, c = 100):
    pass

def my_func1(a,b,c):
    pass

my_func1(10,b = 100,c) ## As we have give b = 100, we can't just say 20 for c. It has to be done like c = 20
my_func1(10,b = 100,c = 20) ## Correct way

def my_func2(a,b = 100, c): ## this will not work. If a positional parameter assigned a default value, every positional parameter after it
                            ## must be assigned a default value
    pass