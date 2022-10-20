
def my_func(a,b):  ## a,b are called as Parameters of my_func
    pass           ## a,b are local to my_func

x = 10
y = 20

my_func(x,y) ## here x,y will be called as argument of my_func
             ## IMP - x,y are passed by reference ie memory address of x,y is passed

def test_func(passArr):
    passArr.append(10)

newArr = [1,2]
test_func(newArr)

print(newArr) ## [1, 2, 10] --- my array got modified.. but why.. because in test_func we passed reference of newArr.
              ## now it will be like passArr and newArr will be pointing to same address. As arrays are mutable, therefore changes made
              ## through reference passArr will also be reflected in newArr