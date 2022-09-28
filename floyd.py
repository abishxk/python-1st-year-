n=int(input('enter a end val:'))
a=1
for i in range(a,n+1):
    print(" ")
    b=a
    for j in range(b,i):
        print(b,end=" ")
        b+=1
    print()
