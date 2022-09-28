l1=eval(input('enter a list:'))
l2=l1.copy()
le=len(l1)
for j in range(le-1):
    for m in range(0,le-1-j):
        if l1[m]>l1[m+1]:
            l1[m],l1[m+1]=l1[m+1],l1[m]
print('sorted list:',l1)
print()
l=[]

for i in l1:
    for k in range(le):
        l.append(l2.index(i)+1)
le2=len(l)
print('new order of arrangement:')
for j in range(0,le2,le):
    print(l[j],end=" ")
print()
print('first word of new arrangement is:',l1[0])
print('last word of new arrangement is:',l1[-1])




