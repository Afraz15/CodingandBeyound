                                #                                         

hi = 'hellothere'
hello = 'hello12'
hey = '1234'
yo = ' should be spaces and newlines'
he = 'Hi'

list1 = [ hi , hello , hey , yo , he]

i = 0

while i < 5:
    print( 'only letters? ' + str(list1[i].isalpha())) # should be no space 
    print( 'only letters and numbers? '  + str(list1[i].isalnum())) 
    print( 'only numbers? ' + str(list1[i].isdecimal())) 
    print( 'only spaces and newlines? ' + str(list1[i].isspace())) 
    print( 'only title? ' + str(list1[i].istitle())) 
    i = i + 1





