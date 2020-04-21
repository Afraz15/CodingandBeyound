                                # REGEXES

import re

phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d')     # this is a single group 
number = phone.search('this is my number : 444-555-4568')
print('my last number was : ' + number.group()) # this .group is a must

hello = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')   # we are making group here
num = hello.search('number : 444-434-1547')
print(num.group())      # empty parameters is equal to (0)
print(num.group(1))     # this is just like how it looks , we are calling the 1st group
print(num.group(0))     # this has the same result like the empty group()
