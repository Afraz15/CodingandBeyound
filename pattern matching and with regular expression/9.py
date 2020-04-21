                            # USING PLUS 

import re

i = re.compile(r'bat(wo)+man')
# I = i.search('i saw batman')
Ii = i.search('i saw batwoman')
II = i.search('i saq batwowowowowowowowowoman')

print(Ii.group(),II.group())




