
## Slicing always return a new object... even if you do slicing in LIST

tempList  = [1,2,3,4,5]
sliceList = tempList[:]

print(id(tempList), id(sliceList))  ## 1831084446088 1831084446600  ... Different memmory address

str = 'python'

str1 = str[:]        ## python
str2 = str[4:1000]   ## on....it will not loop circularly because of 1000.. it will return from postion 4 to last element
str3 = str[0:5:-1]   ## ''... you want to go from 0 to 5 in steps of -1.. it will not work
str4 = str[5:0:-1]   ## nohty... without -1 it will not work.. as we are moving backward
str5 = str[::-1]     ## nohtyp  ... For reversing the string


print(str1 is str)  ## True .... even though Slicing always return a new object
print(str2 is str)  ## False



print(list(str))  ## ['p', 'y', 't', 'h', 'o', 'n']
print(','.join(str)) ## p,y,t,h,o,n ... Demonstration of join
print(','.join(['a','b','c'])) ## a,b,c
##print(','.join([1,2,3])) ## TypeError: sequence item 0: expected str instance, int found

