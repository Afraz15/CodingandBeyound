                        # TIMEOUT , LIMIT , DEFAULT KEYWORD ASSIGNMENT

import pyinputplus as p
'''
i = p.inputNum('enter your lucky number :', limit = 3)
print(i)

I = p.inputNum('enter a num : ', timeout = 2)
print(I)
'''
'''
the code is simple to understand 

limit decides how many times the statement will be repeated

timeout is the time within which the user has to type in the input else it will not be accepted or it will cause error

'''

Ii = p.inputNum('enter a num :', limit = 2, default = 'none')
print(Ii)

'''
default is like a value which will be assigned if there is no value stored in it else the value the user typed will be stored in it

'''





