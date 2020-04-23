                        # INPUT(),GREATER\LESS() AND MIN()

import pyinputplus as p

h = p.inputNum('Enter num: ',min=4)

print(h)

'''
we are asking the user for decimal input which should be greater than 4

'''

H = p.inputNum('enter a num greater than 4 : ', greaterThan = 4)
print(H)

Hi = p.inputNum('enter a num less than 1 : ', lessThan = 1)
print(Hi)




