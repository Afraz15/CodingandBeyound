                        # MATCHING NEW LINE WITH DOT CHARACTER

import re

i = re.compile(r'.*')
I = i.search('save the \n public trust\n here')
print(I.group())

'''
with only .* character it will consider the text after the newline character another group

'''

h = re.compile(r'.*',re.DOTALL)
H = h.search('save the \n public trust\n here')
print(H.group())

'''
using the re.DOTALL character with .* help in applying the escape characters and considering all the words to be the same

'''

hi = re.compile(r'.*',re.DOTALL)
Hi = hi.search('hello\t this\\ is\n me')
print(Hi.group())

