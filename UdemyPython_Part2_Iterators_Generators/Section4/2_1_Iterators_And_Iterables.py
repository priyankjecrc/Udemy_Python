
## Iterator vs Iterable

## Iterator -  1. It is an object that implements a) __iter__ and b) __next__
##             2. Iterators are consumed

## Iterable - 1. It is an object that we can Iterate. It implements __iter__ method and its __iter__ method returns NEW ITERATOR and using that ITERATOR we iterate
##            2. They don't get consumed as they return NEW ITERATOR every time


## IMP -
## For statement in Python always operate on an ITERABLE
## always remember to raise StopIteration in __next__ method





class City():
    def __init__(self, cityList):
        self.cityList = cityList
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if (self.index >= len(self.cityList)):
             raise StopIteration                  ## Why do we raise this Error StopIteration always: That's because StopIteration is the normal,
        else:                                     ## expected signal to tell whomever is iterating that there is nothing more to be produced.
            cityName = self.cityList[self.index]  ## When we use next() while iterating (without using for loop) we will get StopIteration but while iterating using
            self.index += 1                       ## for loop we dont get StopIteration - Because the for loop listens for StopIteration explicitly. It knows that StopIteration has been raised and it's time to stop
            return cityName


upCity = City(['Agra','Alahabad','Mathura','Ghaziabad'])

for i in upCity:
    print(i)

## Agra
## Alahabad
## Mathura
## Ghaziabad

## Problem with upper appraoch - __next__ has been exhausted and we can't use it again on same object. We will have to create new object of City again



## Solution to above probem - let's separate City class and Iterator


class NewCity():
    def __init__(self, cityList):
        self.cityList = cityList



class NewCityIterator():
    def __init__(self, passObj):
        self.passObj = passObj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.index >= len(self.passObj.cityList)):
            raise StopIteration

        else:
            cityName = self.passObj.cityList[self.index]
            self.index +=1
            return cityName

mahCityObj =  NewCity(['Pune','Mumbai','Kolhapur','Latur'])

newCityItrObj = NewCityIterator(mahCityObj)

for i in newCityItrObj:  ## here iterator -> newCityItrObj will get exhausted and can't be used again
    print(i)

## Pune
## Mumbai
## Kolhapur
## Latur


## Problem - Though we have separated City class and Iterator, but we will have to create new Iterator everytime we will to iterate ?

## Can we solve this - If we can do something that will return Iterator automatically so that we can Iterate over easily without bothering to create
## new Iterator object. This is called as Iterable protocol




class NewCountry():
    def __init__(self, countryList):
        self.countryList = countryList

    def __iter__(self):                   ## This is the new addition... We are returning object of Iterator
        return NewCountryIterator(self)



class NewCountryIterator():
    def __init__(self, passObj):
        self.passObj = passObj
        self.index = 0

    '''
    def __iter__(self):           ## Now this __iter__ won't be necessary. But its good to keep it
        return self
    '''

    def __next__(self):
        if(self.index >= len(self.passObj.countryList)):
            raise StopIteration

        else:
            countryName = self.passObj.countryList[self.index]
            self.index +=1
            return countryName


countryObj =  NewCountry(['India','Sweden','USA','Nepal'])

#############################   VV IMP - Check list(countryObj) and compare with list(mahCity) in 2_3 notebook  ################################

print(list(countryObj))  ## ['India', 'Sweden', 'USA', 'Nepal'] ## list will actually iterate over countryObj, therefore we see this formation




for country in countryObj:
    print(country)

## India
## Sweden
## USA
## Nepal

for country in countryObj:
    print(country)

## India
## Sweden
## USA
## Nepal



## One more Example...sets have there own iterators

myset = {10,20,30}

mysetIt = myset.__iter__()

for i in mysetIt:
    print(i)

for y in mysetIt: ## will not do anything because myset gets consumed already in above loop
    print(y)

mylist = [100,200,300]

print(mylist.__getitem__(1))