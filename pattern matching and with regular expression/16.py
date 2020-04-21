                            # DOT-STAR CHARACTER

import re

i = re.compile(r'First Name: (.*) Last Name: (.*)')
I = i.search('First Name: Al Last Name: Sweigart')
print(I.group())

hi = re.compile(r'email: (.*)')
Hi = hi.search('email: asf@gsda.com ')
print(Hi.group())

'''
we can use this .* mathod to call out all the characters we want 
there are two types of Dot characters : .* and .?   
the dot star is a greedy type which means that it will print all the matched characters it can
the dot ? is a non-greedy type and it is the opposite of dot star 

'''

he = re.compile(r'<.*?>')
ha = re.compile(r'<.*>')
He = he.search('hello <this is me> hello>')
HE = ha.search('hello <this is me> hello>')
print(He.group())
'''
this is the non-greedy type 

'''

print(HE.group())

'''
this is the greedy type

'''









