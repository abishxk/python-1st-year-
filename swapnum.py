a=eval(input('enter a list:'))
l=len(a)

for i in a:
    if a.count(i)>1:
        a.remove(i)
print(a)
b=[]
for i in range(l):
    for j in range(1,i+1):
        c=i*j
        b.append(c)
print(b)
