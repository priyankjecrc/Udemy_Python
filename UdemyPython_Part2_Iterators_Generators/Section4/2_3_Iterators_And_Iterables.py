
## Covering video no - 46 function video & 47 - The iter() function coding


class City():
    def __init__(self, cityList):
        self.cityList = cityList

    def __getitem__(self, item):
        return self.cityList[item]


cityList = ['Pune','Mumbai','Akola','Nagpur']

mahCity = City(cityList)


#############################   VV IMP - Check list(mahCity)  and compare with list(countryObj) in 2_1 notebook  ################################

print(list(mahCity))  ## ['Pune', 'Mumbai', 'Akola', 'Nagpur'] .. list will actually iterate over mahCity, therefore we see this formation


print(mahCity[0]) ## Will call __getitem__
                  ## Pune

for city in mahCity: ## Will call __getitem__
    print(city)

## Pune
## Mumbai
## Akola
## Nagpur



mahCityItr = iter(mahCity) ## IMP - This will make mahCity as iterator. As of now don't know HOW ?

print(type(mahCityItr)) ## <class 'iterator'> ... since mahCity has become iterator now, it means we call 'next' on it

print(next(mahCityItr)) ## Pune
print(next(mahCityItr)) ## Mumbai
print(next(mahCityItr)) ## Akola
print(next(mahCityItr)) ## Nagpur
print(next(mahCityItr)) ## Error: StopIteration
