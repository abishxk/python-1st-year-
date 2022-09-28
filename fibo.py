##n=int(input('enter end range:'))
##l=[]
##a=0
##l.append(a)
##for i in range(1,n+1):
##    l.append((i-1)+i)
##print(l)
##    
##
##



#0 1 1 2 3 5 8 13

n=int(input('enter a limit:'))
b=0
c=1
if n>0:
    for i in range(n):
        a=b+c
        print(b,end=' ')
        b=c
        c=a
