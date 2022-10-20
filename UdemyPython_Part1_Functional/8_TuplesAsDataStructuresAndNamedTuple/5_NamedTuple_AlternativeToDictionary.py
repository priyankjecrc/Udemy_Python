## After python 3.6, dicitonary actually maintains insertion order of keys

## Why should i use NamedTuple instead of Dictionary...?
## In dicts, only the keys have to be hashable, not the values. namedtuples don't have keys, so hashability isn't an issue.
## However, they have a more stringent restriction -- their key-equivalents, "field names", have to be strings.


import collections

mydict  = dict(key1 = 100, key2 = 200, key3 = 300, key4 = 400)

dictTuple = collections.namedtuple('DictTuple', mydict.keys()) ## Look at this intelligent way

dicttup1 = dictTuple(*mydict.values()) ## Good but not the best way

dicttup2 = dictTuple(**mydict) ## best way... as this will pass values like key1=100, key2=200, key3=300, key4=400 and we dont have to
                               ## worry about positions of arguments

print(dicttup2.key2) ## 200
print(dicttup2) ## DictTuple(key1=100, key2=200, key3=300, key4=400)

## Strange

print({**mydict}) ## {'key1': 100, 'key2': 200, 'key3': 300, 'key4': 400}.... This works but below doesn't
print(**mydict) ## TypeError: 'key1' is an invalid keyword argument for print()

