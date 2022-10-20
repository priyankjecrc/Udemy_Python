## First Understand difference between mutation and non mutation

mylist = ['eric','john','danny']
mylist = mylist+['michael']         ## ['eric', 'john', 'danny', 'michael'].... This is not mutation.. we are making mylist point to new object

mylist.append('tyrion') ## This is mutation
print()

## List all function
'''
append(x)  Adds an element at the end of the list
clear()	  Removes all the elements from the list
copy()	  Returns a copy of the list
count()	  Returns the number of elements with the specified value

extend(iterable)  Add the elements of a list (or any iterable), to the end of the current list =====> appends adds only 1 element, while this 
                  can add entire sequence. The sequence needs to be iterable.. for eg it can be set as well
                  
index()	  Returns the index of the first element with the specified value
insert(i,x)  Adds an element at the specified position
pop(i)	  Removes the element at the specified position ==> and also return element which was present at ith location
remove(x)  Removes the first occurence of x 
reverse() Reverses the order of the list
sort()	  Sorts the list
copy()   This will do shallow copy.. shallow and deep copy will be discussed later

'''

mylist.extend({'agra','jaipur'})  ## ['eric', 'john', 'danny', 'michael', 'tyrion', 'agra', 'jaipur']
                                  ## order of elements in set may not be guaranteed