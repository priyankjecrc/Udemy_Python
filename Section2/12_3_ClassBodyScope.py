
## Another interesting case

name = 'priyank'

class MyClass():
    name = 'Raymond'

    list1 = [name for i in range(3)]  ## It is actually a comprehension. It is actually a function. Therefore its scope will be
                                      ## nested in the scope which has MyClass. Hence the comprehension will be nested in scope of module 12_3_ClassBodyScope

print(MyClass.list1)    ### ['priyank', 'priyank', 'priyank']