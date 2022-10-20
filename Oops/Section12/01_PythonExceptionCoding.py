
## We don't want to make our exception handlers too broad

ex = Exception()
print(isinstance(ex, object))  ## True

def func1():
    func2()

def func2():
    func3()

def func3():
    ex = ValueError('some custom message')
    raise ex

func1()  ## Remember call stack trace.. Origin of the call is at bottom....Latest call is at top of stack

'''
Traceback (most recent call last):
  File "C:\Users\japr01\PycharmProjects\Udemy_Python_OOPS\Section12\01_PythonExceptionCoding.py", line 15, in <module>
    func1()  ## Remember call stack trace.. Origin of the call is at bottom....Latest call is at top of stack
  File "C:\Users\japr01\PycharmProjects\Udemy_Python_OOPS\Section12\01_PythonExceptionCoding.py", line 6, in func1
    func2()
  File "C:\Users\japr01\PycharmProjects\Udemy_Python_OOPS\Section12\01_PythonExceptionCoding.py", line 9, in func2
    func3()
  File "C:\Users\japr01\PycharmProjects\Udemy_Python_OOPS\Section12\01_PythonExceptionCoding.py", line 13, in func3
    raise ex
ValueError: some custom message 
'''

## We can stop propagation of error. Let's stop propagation of error in func2()

'''
def func2():
    try:               
        func3() 
    except ValueError:              ## Now there will be no stack trace as we have silenced the exception and propagation is stopped
        print('Error Occured - Silencing it')
        
'''