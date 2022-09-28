print("**********ENTER TIME IN BEIJING************")
hour=int(input('hour:'))
mi=int(input('minutes:'))
meri=input('meridiem(am/pm):')

if hour<13:
    if meri=='am':
        nt=hour+6
        if nt>12:
            print('time in berlin is:',nt-12,':',mi,'pm')
        else:
            print('time in berlin is:',nt,':',m,'am')
    elif meri=="pm":
        c=a+6
        if c>12:
            print('time in berlin is:',nt-12,":",m,'am')
        else:
            print('time in berlin is:',nt,':',m,'pm')
else:
    print('enter the time in 12hr format')
    

