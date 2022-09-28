a=int(input('enter number of rows:'))
b=int(input('enter number of column:'))
c=input('enter a symbol to print:')
for i in range(a):
    for j in range(b+1):
        if (i==0 or i==a-1 or j==0 or j==b):
            print(c,end=" ")
        else:
            print(("  ",end=" ")," ")
    print()
