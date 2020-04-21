                                # MAKING CHARACTER CLASS

import re

i = re.compile(r'[aeiouAEIOU]')
I = i.findall('hello there , name\'s --- ')
print(I)

'''
special characters like : +*&% are not allowed in it and you cannot use a backslash as well ...
the only mathods are like : 0-4 which means zero to four and it will be written like : [0-4]

there is also another mathod through which we can print out the values in the statement which does not include the values which we have given ; it's example is given below

'''

j = re.compile(r'[^aeiouAEIOU]')
J = j.findall('hello world and nature')
print(J)

