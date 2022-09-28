def loginn(name):
    pas=input('enter a password with 6 characters:')
    a=len(pas)
    if 6>a:
        print('invalid password ;(')
        loginn(name)
    elif pas==name:
        print('password cannot be your username... choose a different password :(')
        login(name)
    else:
        print('signing up...')
def login(name):
    pas=input('enter a password:')
    a=len(pas)
    if 6>a:
        print('invalid password ;(')
        loginn(name)
    elif pas==name:
        print('password cannot be your username... choose a different password :(')
        loginn(name)
    else:
         print('signing up...')
        
name=input('enter a username:')
login(name)
