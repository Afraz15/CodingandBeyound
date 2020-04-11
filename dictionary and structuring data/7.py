                                # USING GET()

picnic = {'fruit': 8,'bottle': 2}

print('we are going to picnic with ' + str(picnic.get('fruit',0)) + 'and ' + str(picnic.get('bottle',0)))       # using str() is important to use the get() command
                     # the get() checks if the value is in the dic and if it is not there then it will return the value which we have given like get('fruit', 0) which is 0 here...   


grow = {'rose': 3, 'sunflower': 10, 'colyflower': 10}

print('we are growing ' + str(grow.get('rose',0)) + ' roses ' + str(grow.get('sunflower',0)) + ' sunflower ' )












