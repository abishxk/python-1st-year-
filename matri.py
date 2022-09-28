m1=[['j','u','g','r','z'],['g','r','z','j','u'],['z','j','u','g','r'],['u','g','r','z','j'],['r','z','j','u','g']]
m2=[['e','m','d','n','o'],['d','e','o','m','n'],['o','n','e','d','m'],['n','o','m','e','d'],['m','d','n','o','e']]
le=len(m1)
le2=len(m2)
print('positions of J:')
for i in range(0,le):
    for j in range(le):
        if m1[i][j]=='j':
            print(i,j,sep=',',end='  ')
print()
print('positions of U:')
for i in range(0,le):
    for j in range(le):
        if m1[i][j]=='u':
            print(i,j,sep=',',end='  ')
print()
print('positions of  D:')
for i in range(0,le2):
    for j in range(le2):
        if m2[i][j]=='d':
            print(i,j,sep=',',end='  ')
print()
print('positions of G')
for i in range(0,le):
    for j in range(le):
        if m1[i][j]=='g':
            print(i,j,sep=',',end='  ')
print()
print('positions of E:')
for i in range(0,le2):
    for j in range(le2):
        if m2[i][j]=='e':
            print(i,j,sep=',',end='  ')
print()
