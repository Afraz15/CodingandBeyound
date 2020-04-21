                            # USING SUB()

import re

i = re.compile(r'Agent (\w)\w*')
I = i.sub(r'\1****','Agent alice is good friends with Agent mark and Agent lewis')
print(I)




