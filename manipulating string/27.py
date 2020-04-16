                            # FIRST BIG PROGRAM

text = {'agree':"""Yes, i agree with your idea""", 'busy':"""sorry but can we do this later this week or next week...""", 'upsell':"""would you consider making it a monthly donation?"""}

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyboard] - copy phrase text ')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('text for ' + keyphrase + ' copied to clipboard.')
else:
    print('there is no text for ' + keyphrase)












