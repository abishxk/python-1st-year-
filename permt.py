from itertools import permutations
A=int(input('enter a number:'))
B=int(input('enter another number:'))
C=A+B
a=bin(A)
b=bin(B)
c=bin(C)
count=0
l1=[]
l2=[]
l3=[]
l4=[]
a1=permutations(a)
b1=permutations(b)
for i in list(a1):
       l1.append(''.join(i))
for j in list(b1):
      l2.append(''.join(j))
for n in l1:
    if n[1]=='b':
        if n[0]=='0':
            l3.append(n)
for o in l2:
    if o[1]=='b':
        if o[0]=='0':
            l4.append(o)
for k in l3:
    for m in range(len(l4)):
         intsum=int(k,2)+int(l4[m],2)
         binsum=bin(intsum)
         if binsum==c:
             count+=1
print('the number of times the bits can be shuffle to get the same sum is ',count)
