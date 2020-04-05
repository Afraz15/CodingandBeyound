                                    # SORTING VALUES IN THE LIST

spam = [2, 4, 3, 5, 1]
spam.sort()                         # this will sort out the numbers in it....
print(spam)

Spam = ['pubg', 'fortnite', 'freefire', 'css']
Spam.sort()                         # this will sort out letters in it....
print(Spam)

sPam = ['pubg', 'fortnite', 'freefire', 'css']
sPam.sort(reverse=True)             # using reverse=True will sort out the letter in z->a 
print(sPam)

spAm = ['pubg', 'fortnite', 'freefire', 'css', 'Apple', 'Dretch', 'Float']
spAm.sort()                         # if the list have mix (capital and small) letters than the capital one will be listed as first...
print(spAm)

spaM = ['pubg', 'fortnite', 'freefire', 'css', 1, 2]
spaM.sort()                         # a list with letters and numbers cannot be sorted...
print(spaM)


