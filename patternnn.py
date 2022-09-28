n=int(input('enter number of rows:'))
x=1
for i in range (1,n+1):
    for j in range(1,i+1):
        print(x**2,end=' ')
        x+=1
    print()
    