                                #  FINDALL NUMBERS

import re

i = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
I = i.search('my numbers are : 456-415-4152 and 415-475-4587 ')
print(I.group())

'''
this is only displaying one number but there is more than one number with the same requirements

'''
j = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
J = j.findall('my numbers are : 456-415-4152 and 415-475-4587 ')
print(J)


h = re.compile(r'(\(\d\d\d\)) \d\d\d-\d\d\d\d')
H = h.findall('my numbers are : (456) 415-4152 and 415-475-4587 ')
print(H)

''' 
there should not be a group else it will display the group() like the above one and we also used an escape character in that which was not needed

'''

k = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
K = k.findall('my numbers are : 456-415-4152 and 415-475-4587 ')
print(K)

'''
this is how a group one looks like and the output of it will also be in group

'''




