                        # MATCHING GROUPS WITH PIPE

import re

hi = re.compile(r'bat(wings|eyes|pants)')
Hi = hi.search('i saw a batwings with pants')
HI = hi.search('bat batpants batwings')
print(Hi.group())
print(HI.group()) 






