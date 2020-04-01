                                # CALLING FUNCTION

def a():                    
    print('a() starts')     # 1. prints this...    
    b()                     # 2. goes to b()
    d()                     # 8. goes to d()
    print('a() returns')    # 12. print this... and ends the program because we only called a()

def b():                        
    print('b() starts')     # 3. print this...
    c()                     # 4. goes to c()
    print('b() starts')

def c():
    print('c() starts')     # 5. print this...
    print('c() returns')    # 6. print this...
                            # 7. returns to a()/2. because there is nothing to execute next
def d():                    
    print('d() starts')     # 9. print this...
    print('d() returns')    # 10. print this...
                            # 11. goes back to a()/8. because there is nothing to execute next

a()
