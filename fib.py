n=int(input('enter a limit:'))
b=0
c=1
if n>0:
    for i in range(n+1):
        a=b+c
        print(b,end=' ')
        b,c=c,a
