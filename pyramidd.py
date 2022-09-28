a=int(input('enter rows:'))
b='*'
for i in range(a,0,-1):
    for j in range(i):
        print(b,end='')
    print()
