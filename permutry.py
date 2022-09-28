from itertools import permutations
a=int(input('enter a num:'))
b=int(input('enter another num:'))
c=a+b
count=0
a1=bin(a)
b1=bin(b)
c1=bin(c)
a2=permutations(a1)
b2=permutations(b1)
l1=[]
l2=[]
l3=[]
l4=[]
for i in list(a2):
    l1.append(''.join(i))
for j in list(b2):
    l2.append(''.join(j))
for k in l1:
    if k[0]=='0':
        if k[1]=='b':
            l3.append(k)
for u in l2:
    if u[0]=='0':
        if u[1]=='b':
            l4.append(u)
for o in l3:
    for m in range(len(l4)):
         intsum=int(o,2)+int(l4[m],2)
         binsum=bin(intsum)
         if binsum==c1:
             count+=1
print('number of permutations:',count)
            
            
