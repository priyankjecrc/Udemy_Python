
class Person():
    human = 'man'
    pass

p = Person()

## I wish to create an attribute named as 'man'
## but I dont want to create using p.man. I wish to make use of human attribute declared inside class

x = p.human

p.x = 'pinkoo'  ## here value of x = 'man'. When I use p.x it will not mean p.man. Therefore i can't create an attribute named as 'man' this way

setattr(p,x,'pinkoo') ## or setattr(p,p.human,'pinkoo')  -  both of them will create an attribute names as 'man'

print(p.__dict__) ##
p.human = p
setattr(p,p.human,100)


