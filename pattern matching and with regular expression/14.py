                        # CARROT AND DOLLAR SIGN

import re

i = re.compile(r'^hello') 
j = i.findall('hello, this is me')
print(j)

'''
the caret is used when we want regex to start from a specific thing...

'''

h = re.compile(r'\d$')
H = h.findall('hello, this is me15')
print(H)

'''
the dollar is used to if we want regex to end with a specific thing...
just like the above programs and the one above this comment; it print out the number (note that it is only number) which the word has with it 

'''

k = re.compile(r'^\d+$')
K = k.findall('45487')
print(K)

hi = k.findall('45d45568')
Hi = k.findall('45 45568')
print(hi,Hi)
'''
it seems that the numbers program work only if there are only numbers in the findall parameters and the last two programs or statements are invalid because one of them has a letter in it and the other one has space in it which make it in two words which is also invalid

'''


