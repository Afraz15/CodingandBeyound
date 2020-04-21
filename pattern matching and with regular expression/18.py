                                # CASE SENSITIVE MATCHING

import re

h = re.compile(r'Hello',re.I)
H = h.search('hello this is me')
print(H.group())

'''
we can use re.I if we want to ignore the upper or lower case 

'''
hi = re.compile(r'HELLO',re.I)
Hi = hi.search('heLLO this is me')
print(Hi.group())
    












