
## Python functions are pass by reference.. It means memmory address is passed to functions

def sampleFunc(passList):
    passList.append('India')


myList = ['Australia', 'Japan', 'USA']  ## myList has the memmory address of ['Australia', 'Japan', 'USA']

print(myList)  ## ['Australia', 'Japan', 'USA'] ... No surprises

sampleFunc(myList)

print(myList)  ## ['Australia', 'Japan', 'USA', 'India']...We can see that 'India' has been added to the list.
               ## This happened because 'Reference' or Memmory Address of ['Australia', 'Japan', 'USA'] is passed in the sampleFunc
               ## passList in sampleFunc will point to Memmory Address of ['Australia', 'Japan', 'USA']...
               ## Therefore any changes happened at the memmory address inside sampleFunc() will be reflected in myList.

## Mutable objects always have above mentioned kind of risk


list1 = [1,2,3,'pinkoo']
print(list1)                 ## [1, 2, 3, 'pinkoo']
print(hex(id(list1)))        ## 0x1babc825388

list1[3] = 'swati'
print(list1)                ## [1, 2, 3, 'swati'] ..... list1 has changed
print(hex(id(list1)))       ## 0x1babc825388 ... Same as above, though the list1 has changed
                            ## This is because list1 points to memmory address of [1,2,3,'pinkoo'].
                            ## When we replace 'pinkoo' with 'swati', we are actually not messing up with the memmory address
                            ## list1 was pointing to. It's just that list present at that memmory address has gone through some modification
