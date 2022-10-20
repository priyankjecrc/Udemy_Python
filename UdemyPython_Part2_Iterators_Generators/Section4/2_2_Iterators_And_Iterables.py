
## https://www.pythontutorial.net/advanced-python/python-iter/

## Understanding __getitem__ and __iter__

## __getitem__ is a sequence protocol
## __iter__ is an iterable protocol

## If __iter__ is not there than __getitem__ is looked out for. First look will be into __iter__

## IMP -
## For statement in Python always operate on an ITERABLE



class NewCity():
    def __init__(self, cityList):
        self.cityList = cityList



class NewCityIterator():
    def __init__(self, passObj):
        self.passObj = passObj
        self.index = 0

    '''
    def __iter__(self):
        return self
    '''

    def __getitem__(self, item):   ## Since __iter__ is commented out therefore __getitem__ is looked out. can be checked by using debugger
        print(item)                ## as __iter__ is commented out, hence __next__ will not be used

        return self.passObj.cityList[item] ## Important to notice that 'item' gets incremented automatically
                                           ## Confusion - when value of item = 4, then error - "list index out of range" must be thrown...
                                           ## Exception is occurring here(can be caught by using try block) but its not getting thrown... But Why ?
                                           ## Because For loops expect that an IndexError will be raised for illegal indexes to allow proper detection of the end of the sequence.

    def __next__(self):
        if(self.index >= len(self.passObj.cityList)):
            raise StopIteration

        else:
            cityName = self.passObj.cityList[self.index]
            self.index +=1
            return cityName


mahCityObj =  NewCity(['Pune','Mumbai','Kolhapur','Latur'])

newCityItrObj = NewCityIterator(mahCityObj)

print(newCityItrObj[0])  ## This will call __getitem__ automatically and not __iter__, even if __iter__ is NOT commented

for i in newCityItrObj: ## How For statement is working here ? We have not implemented __iter__() and For statement in Python always operate on an ITERABLE
                        ## than how is it working ?
    print(i)            ## The for loop doesn't know how to iterate over your object specifically because you have not implemented __iter__(),
                        ## so it uses the default iterator which I believe calls __getitem__. This starts at index 0 and goes until it gets an IndexError


