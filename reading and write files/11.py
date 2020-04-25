                                # READ AND WRITE 

from pathlib import Path

i = Path('text.txt')

i.write_text('hello world')
print(i)

print(i.read_text())

i.write_text('morning')

print(i.read_text())

'''
using the read and write mathod we can create a dir , write text in it and then read it as well but if we use write command again in 

'''




