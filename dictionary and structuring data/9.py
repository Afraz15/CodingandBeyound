                               # COUNT CHARACTER PROGRAM

message = 'This is a way down to the basement where that piano is played at night to scare away all the animals near the house'

count = {}                 # this is an empty dic

for character in message:               # it will go through all the characters in message
    count.setdefault(character,0)       # this will make the dic in count
    count[character] = count[character] + 1     # it is adding a number in the count

print(count)






























