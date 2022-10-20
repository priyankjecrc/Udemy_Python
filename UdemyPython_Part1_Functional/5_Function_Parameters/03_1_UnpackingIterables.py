
## 1,2,3 - is also an tuple
## (1,2,3) - is also an tuple. Paranthesis are given just to give clarity

## (1) -> means 1, not a tuple
## (1,) -> means tuple

## Packed Values - The values which are bundled together in some way
## tuples, list, set, dict are obivious

a,b = 100,200

b,a = a,b

print(a,b) ## 200 100


a,b,c = [10,20,30]
print(b) ## 20

a,b,c = 'XYZ'
print(b) ## Y


a,b,c = 'XYZK'
print(b) ## ValueError: too many values to unpack (expected 3)

## In dictionary when we iterate, we just iterate through keys. So when we unpack dict, we are actually unpacking keys not values


d = {'key1':1, 'key2':2, 'key3':3 }

a,b,c = d ## IMP - As dict stores key in unordered fashion therefore. a = 'key1' or 'key2' or 'key3' likewise for b and c
          ## but we can iterate through dictionary values by using d.values(), but again the order is not gauranteed

## Above mentioned things will also happen in case of sets as values are not stored in ordered way in sets