
## Zip_longest vs zip


from itertools import zip_longest

l1 = [10,20,30]

l2 = ['a','b','c','d','e']

print(list(zip(l1,l2)))  ## [(10, 'a'), (20, 'b'), (30, 'c')]

print(list(zip_longest(l1,l2,fillvalue='Not Present'))) ## [(10, 'a'), (20, 'b'), (30, 'c'), ('Not Present', 'd'), ('Not Present', 'e')]

## See the difference in o/p above... zip will limit itself to the shortest iterable, while zip_longest will NOT do that