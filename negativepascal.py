from math import factorial
l=[]
l2=[]
n=int(input('enter a end value:'))
for i in range(n):
    for j in  range(i+1):
        l.append(factorial(i)//(factorial(j)*factorial(i-j)))
print(l)
c=2
e=2
o=1
x=0
a=0
for i in range(1,len(l)+1):
    if x%i==0 or x==0:
        if i%2!=0:
            for j in range(a,len(l)+1,e):
                print(j)
                x+=2
                a=j
        elif i%2==0:
            for k in range (a,len(l)+1,1):
                x+=2
                a=j
                print(k)
            
    
    
