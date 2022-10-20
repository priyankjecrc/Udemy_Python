# Tuples are immutable & because of this -  Length of Tuples cannot change , Their order is fixed
# We actually don't need parenthesis to pack a tuple

city,_, population = ('agra','india', 2500000) ## We only wish to unpack city and population

## best way to unpack a big tuple

record  = ('Priyank',32,'agra','india', 2500000, 'Asia', 'SMS group')

name, *_ ,company = record
name, *ignored ,company = record

## _ or ignored - they will be list

print(_) ## 32 agra india 2500000 Asia
print(type(_)) ## <class 'list'>
print(name) ## Priyank
print(company) ## SMS group

for record in enumerate(('agra','delhi','pune','jaipur','kerala')):
    print(record)

## o/p - every record will be a tuple with index
'''
(0, 'agra')
(1, 'delhi')
(2, 'pune')
(3, 'jaipur')
(4, 'kerala')
'''

## better way

for index, city in enumerate(('agra','delhi','pune','jaipur','kerala')):
    print(f' Index {index} --- {city}')

## O/P

'''
 Index 0 --- agra
 Index 1 --- delhi
 Index 2 --- pune
 Index 3 --- jaipur
 Index 4 --- kerala
'''