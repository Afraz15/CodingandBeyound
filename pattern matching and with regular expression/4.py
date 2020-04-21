                            # USING ALL THE ESCAPE CHARACTERS
import re


boy = re.compile(r'\+(\d\d) (\d\d\d-\d\d\d\d\d\d\d)')
num = boy.search('my number is : +92 308-0113605')
print(('this is my current number : ') + num.group())

a = re.compile(r'.(\d\d) (\d\d\d-\d\d\d\d\d\d\d)')
A = a.search('my number is .92 308-0113601')
print('my current number is : '  + A.group())

hi = re.compile(r'\[\d\d\d\] (\d\d\d-\d\d\d\d)')
Hi = hi.search('hello there [441] 454-5824')
print(Hi.group())


