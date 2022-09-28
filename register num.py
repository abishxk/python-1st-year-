##21vite1000
a=input('enter your register numbers:')
b=a[0:2]
c=a[2:6]
d=a[6:10]
##print(b,c,d)
if b.isdigit():
    if c.isalpha():
        if d.isdigit():
            print('match found')
else:
    print('match not found')


    
