                                # OPTIONAL MATCHING

import re

hi = re.compile(r'bat(wo)?man')     # this paranthsis means that if the value in the statement has wo in the start and if it does then it will also write wo with it else it won't
Hi = hi.search('i saw batwoman!')
print(Hi.group())

ji = re.compile(r'bat(wo)?man')
Ji = ji.search('i saw batman with batwoman')
print(Ji.group())