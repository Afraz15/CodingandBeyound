                        # FINDING NUMBER USING PROGRAM


def phone(text):
    if len(text) != 12:
        return False
    for i in range (0,3):       # this 'i' means that i want to count from 0 to 3 and set i to current loop which also means that each time the loop will run it will change the value of 'i'...
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

message = 'you should call on this number : 444-555-6666 ; this is my office number : 444-555-1235'

for i in range(len(message)):
    chunk = message[i:i+12]         
    if phone(chunk):
        print('phone number found : ' + chunk)
print('done')

''' in the chunk : when it first starts the value of i will be 0 and so mess[0:12] and next time value of i will be 1 and mess[1:13] ; all in all the phone() function is used and it will start finding the value in the message which has 12 letters and a single word which will be a number of course... '''

