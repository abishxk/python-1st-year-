from itertools import permutations
A=int(input('enter a number:'))
B=int(input('enter another number:'))
C=A+B
a=bin(A)
b=bin(B)
c=bin(C)
##print(a)
##print(b)
##print(c)
c1=str(c)
a1=str(a)
b1=str(b)
c2=c1[2:]
a2=a1[2:]
b2=b1[2:]
##print(a2)
##print(b2)
##print(c2)
a3=int(a2)
b3=int(b2)
c3=int(c2)
count=0
ok=0
l1=[]
l2=[]
l3=[]
l4=[]
a4=permutations(a2)
b4=permutations(b2)
for i in list(a4):
       l1.append(''.join(i))
#print(l1)
for j in list(b4):
      l2.append(''.join(j))
#print(l2)       
for z in l1:
    l3.append(int(z))
print(l3)
for y in l2:
    l4.append(int(y))
print(l4)
for k in range(len(l1)):
    for m in range(k):
        intsum=int(k,2)+int(m,2)
        print(intsum)
        binsum=bin(intsum)
        if binsum==c:
            c+=1
print(count)
