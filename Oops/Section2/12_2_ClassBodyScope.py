
## Another interesting example

kingdom = 'Humania'
phylum = 'Humadata'
family = 'Humaidae'

def anyMethod():

    kingdom = 'Animalia'
    phylum = 'chordata'
    family = 'pythonidae'


    class MyClass():

        kingdom = 'Alienaa'

        def say_hello(self):
            print(kingdom)   ## Imp - Which kingdom will be picked ??
                             ## say_hello is defined in MyClass which is nested in scope of funtion anyMethod()
                             ## hence say_hello will be nested in scope of function anyMethod(). Therefore Animalia as kingdom value will be picked

    return MyClass()





obj = anyMethod()
obj.say_hello()       ## Animalia

