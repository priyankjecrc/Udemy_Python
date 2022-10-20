
## Counting no of times a Function has been called

def funcCounter(passFunc):
    counter = 0

    def returnFunc(*args):
        nonlocal counter
        counter = counter+1
        print(f'Function: {passFunc.__name__} has been called {counter} times')
        return passFunc(*args)

    return returnFunc

def addVal(a,b):
    return a+b

fnAdd = funcCounter(addVal)

print(fnAdd(3,5))
print(fnAdd(2,5))
