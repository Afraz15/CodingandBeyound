                            # ALLOW/BLOCK REGEXES

import pyinputplus as p

i = p.inputNum(allowRegexes = [r'[02468]$'])
print(i)

'''
we are allowing the program the program to use the regex

'''

I = p.inputNum(allowRegexes = [r'(X|L|V|J|H|K)+', r'zero'])
Ii = p.inputNum(blockRegexes = [r'(X|L|V|J|H|K)+', r'zero'])
print(I)
print(Ii)

'''
here we are allowing the program and on the other line we are blocking it with another variable

'''



