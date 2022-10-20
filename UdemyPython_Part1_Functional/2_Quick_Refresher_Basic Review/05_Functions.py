
## Watch video after 6.28 mins. Same reference has been made in Udemy_Python_OOPS section 12, 01_PythonExceptions.py

def myfunc():  ## Python is just creating a function right now.. Its not running them
    print(i)

myfunc() ## NameError: name 'i' is not defined. Now myfunc() is running it will need access to i, but i is not defined yet. Therefore it will give error

i = 5

myfunc() ## 5. Now myfunc() is running it will need access to i, but i is already defined. Therefor no error