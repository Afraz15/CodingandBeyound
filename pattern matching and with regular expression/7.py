                                    # USING THE OPTIONAL MATHOD FOR NUMBERS

import re

hi = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
Hi = hi.search('my number is : 456-5555')                       
print(Hi.group())


i = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
j = i.search('my number is : 145-555-4587')
print(j.group())

hello = re.compile(r'(\(\d\d\d\))? \d\d\d-\d\d\d\d')
bb = hello.search('my number is : (454) 458-4715')
print(bb.group())

''' 
we can even use the escape characters in this just like the last program ; this is just like the last programs that we did but the difference is just that we use question  mark in it and it will work like an optional program...

'''

