                        # USING THE SHORTHAND CHARACTERS

import re

i = re.compile(r'\d+\s\w+')
I = i.findall('1 chocolate, 2 bananas, 3 apples and 9 cakes :p')
print(I)

'''
in this program we are looking for numbers (\d) after that space (\s) and then letters (\w) and adding plus (+) will result in printing all the letters present after word...

'''


