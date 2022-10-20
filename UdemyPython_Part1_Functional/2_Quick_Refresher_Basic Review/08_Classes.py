
## Few things discussed in this chapter, but only following looks considerable

## Good to know difference between type() and isinstance()
## isinstance considers inheritance, while type() doesn't


class parentClass():
    pass

class childClass(parentClass):
    pass

childObj1 = childClass()
parentObj = parentClass()

print(type(childObj1) is childClass) ## True
print(type(childObj1) is parentClass) ## False   ## type() is not considering inheritance
print(isinstance(childObj1,childClass)) ## True
print(isinstance(childObj1,parentClass)) ## True  ## isinstance() is considering inheritance

