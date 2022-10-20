
## Skipped Video no 107 to 116 .. all are on Decorators..
## Go through them in free time

def outerFunc(passfunc):

    def innerfunc():
        return 'inside innerfunc()'

    return innerfunc



somefunc = outerFunc(lambda x:x+10)

print(somefunc.__name__)