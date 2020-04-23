                            # INPUTCUSTOM()

import pyinputplus as p

def addupto(num):
    numlist = list(num)
    for i, digit in enumerate(numlist):
        numlist[i] = int(digit)
    if sum(numlist) != 10:
        raise Exception('The digit must be add up to 10 and not %s.'%(sum(numlist)))
        return int(num)

i = p.inputCustom(addupto)


