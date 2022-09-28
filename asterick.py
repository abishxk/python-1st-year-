def pattern(row):
    num=1
    for i in range(row):
        for j in range(i+1):
            print('*',end="")
        print()
def nrettap(row):
    num=row
    for i in range(row,0,-1):
        for j in range(0,i-1):
            print('*',end="")
        print()
    

row=int(input('enter number of rows:'))
pattern(row)
nrettap(row)
