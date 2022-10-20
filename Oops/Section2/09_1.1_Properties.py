## Properties are different than attributes
## Python does not have facility of declaring attribute as private, like in java.
## Therefore any attribute will be exposed to outer world. In java if a variable is declared private we can access it by getters and setters
## if they are declared

## Any way in python exposing attributes to end user is normal in python. But this actually brings another problem
## If in future it is required to internally make some changes in the attribute. As endusers are using it directly it may cause error for them
## Therefore it make sense to use getter and setter. But using getter and setter again in the code to set and get values is not python style
## Python style is to access using .(dot) notation.

## Python property class maintains python style of using .(dot) notation. Using property class we can use .(dot) notation but in the backend
## access will be allowed by getter and setter

##  It’s common to refer to property() as a built-in function. However, property is a class designed to work as a function rather than as a
## regular class. That’s why most Python developers call it a function.

class MyClass():

    def __init__(self,language):
        self._language = language   ## Python convention to let end users know not to mess with _language

    def __getLanguage(self):
        return self._language

    def __setLanguage(self, value):
        self._language = value

    language = property(fget=__getLanguage, fset=__setLanguage)  ## here using property we are attaching getter and setter to language which
                                                                 ## is a class attribute

    lang = property()                        ## Another way to use
    lang = lang.getter(__getLanguage)        ## see how lang.getter is reassigned to lang. Error will be thrown if it is not reassigned to lang
    lang = lang.setter(__setLanguage)

obj = MyClass('Python')

print(obj.language)  ## This will call __getLanguage automatically
print(obj.lang) ## ## This will also call __getLanguage automatically


print(obj.__dict__)  ## {'_language': 'Python'} .This will contain _language because of self._language

## Imp -
## Let's play a trick. Since object dict is mutable we can add attribute language as shown below

obj.__dict__['language'] = 'Java'

print(obj.__dict__)  ## {'_language': 'Python', 'language': 'Java'}. attribute language has been added

## now when we call obj.language -> should python be returned or java be returned ?

print(obj.language) ## Python will be returned . Even if we have an instance attribute that has same name as property
                    ## instance attribute won't be called. Python will still use the property defined at class level to
                    ## get the value


## Now try this

obj.__dict__['_language'] = 'C++' ## Check the results for this
print(obj.language)


