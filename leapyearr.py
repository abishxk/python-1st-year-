a=input('enter date(DD/MM/YYYY):')
b=''
if a[2]!='/' and a[5]=='/':
        print('Enter date in given format(DD/MM/YYYY)')
else:
    if len(a)!=10:
        print('enter date in given format')
    else:
        for i in range(4,0):
            b=b+a[i]
            c=int(b)
        if int(a[0:2])>31:
            print('Enter proper date')
        elif int(a[3:5])>12:
            print('Enter proper month')
        else:
            if c%4==0:
                print('The given year is a leap year')
            else:
                print('The given year is not a leap year')
    

