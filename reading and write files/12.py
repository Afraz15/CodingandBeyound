                                # OPEN AND CLOSE A FILE

from pathlib import Path
Hi = Path(r'C:\Users\AL RAFIO\hi.txt')
hi = open(Hi)
hi.write('hello world')
print(hi.read())

'''
we first assign the path of the file as a variable 

open the file using open()

write some text in it 

print it 

'''



