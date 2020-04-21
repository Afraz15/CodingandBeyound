                            # SPECIFIC REPEATIONS USING BRACES

import re

i = re.compile(r'(HA){3,9}')
I = i.search('HAHAHAHA')
print(I.group())

Ii = i.search('HAHA')
print(Ii == None )      # checking if it's true


''' 
this is something we want something to be repeated for a specific times and no more 

'''