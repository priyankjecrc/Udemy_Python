## IMP... usefule


list1 = ['pinkoo','kannu','Swati','Mummy']
print(sorted(list1))  ## ['Mummy', 'Swati', 'kannu', 'pinkoo']... not inplace sort
                      ## Here sorting is done by Character code of First Letter

print(ord('M'), ord('S'), ord('k'), ord('p'))  ## 77 83 107 112... sorting is done based on this

print(list1)  ## ['pinkoo', 'kannu', 'Swati', 'Mummy']


## Lets say we want to sort by avoiding upper or lower case...ie we want to sort like in telephone dictionary



print(sorted(list1, key= lambda x:x.upper())) ## ['kannu', 'Mummy', 'pinkoo', 'Swati']
print(sorted(list1, key = lambda x:x.lower())) ## ['kannu', 'Mummy', 'pinkoo', 'Swati'] ... both will give same result


## Another example of sorting

mydict = {'pinkoo':100,'kannu':200,'Swati':50,'Mummy':150}

print(sorted(list1, key=lambda x:mydict[x])) ## ['Swati', 'pinkoo', 'Mummy', 'kannu'] ... sorting by order in dictionary