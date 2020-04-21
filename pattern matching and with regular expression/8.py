                                # MATCHING 0 OR MORE WITH STARS
import re

i = re.compile(r'bat(wo)*man')
I = i.search('i saw batman')
Ii = i.search('i saw batwoman')
II = i.search('i saw batwowowowowowowowoman')

print(I.group(),Ii.group(),II.group())

''' 
the star mean that if something match then print it and if the word which is in the parentheses is repeaded multiple times then it will print that as well 

'''


