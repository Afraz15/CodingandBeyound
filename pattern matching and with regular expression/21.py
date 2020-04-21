                            #   PHONE AND EMAIL PROJECT

import re,pyperclip

phone = re.compile(r'''(
    (\d{3}|\(\d{3}\)))?             # area code
    (\s|-|\.)?                      # seperator 
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # seperator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,3}))?  # extension
    )''',re.VERBOSE)






'''
in the area code , the code can be any 3 digits and if it is in parameters then the other one will be used and we seperate them with piper or 'bitwise or' operator

in the seperator, it can be any space, hyphen or a period and we seperate them with a bitwise or operator

'''

email = re.compile(r'''([a-zA-Z0-9._%-+]+   # username
    @                                       # @ symbol  
    [a-zA-Z0-9.-]+                          # domain name
    (\.[a-zA-Z]{2,4})                       # dot-something
    )''',re.VERBOSE)

'''
username can be anything : lower or upper case letter with symbols

the username and domain are seperated by @

domain name is the same as username but have less symbol choice

'''

text = str(pyperclip.paste())

matches = []

for groups in phone.findall(text):
    num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        num += 'x' + groups[8]
    matches.append(num)
for groups in email.findall(text):
    matches.append(groups[0])

'''
this is understandable that this is the part where we store all the values in group

'''

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email found')











