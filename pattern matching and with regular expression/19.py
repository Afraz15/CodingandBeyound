                                # SUBSTITUTING STRING WITH SUB()

import re

i = re.compile(r'Agent \w+')
I = i.sub('cencored','Agent Alice is good friend with Agent Mark')
print(I)

'''
we can hide the text we want using this mathod 

using \w+ will hide the text which is -----\w+ and also hide a single word which is written right after the text we want to hide just like the above program...

using sub() in the next line and putting the word we want to replace it with the hidden text will make it more understanding else it will look awkward

space after the text and the replacing of word is a must

'''

hi = re.compile(r'goat \w+')
Hi = hi.sub('','there were many goat over there and all of them were quite healthy')
print(Hi)

