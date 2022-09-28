year=int(input('enter a year:'))

if year%4==0:
    a=year+28
    print(a)
elif year%4==2:
    b=year+11
    print(b)
elif year%4==3:
    c=year+5
    print(c)
elif year%4==1:
    d=year+6
    print(d)
else:
    print('invalid input')
    
        
        
