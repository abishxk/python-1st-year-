e=int(input('enter a end limit:'))
c=0
b=1
for i in range(1,e+1):
    a=i**3
    c+=1
    if c==e:
        print(a,end=" ")
    else:
        print(a,end=',')
    
