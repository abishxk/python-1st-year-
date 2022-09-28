a=[]
n=0
while n!=-1:
    n=int(input('enter a number:'))
    a.append(n)
print(a)
le=len(a)

positive_total=0
pos=[]
for i in a:
    if i>0:
        pos.append(i)
        positive_total+=i
positive_average=positive_total/len(pos)
print(f"the average of given positive numbers is {positive_average}")

b=a.remove(-1)

negative_total=0
neg=[]
for i in a:
    if i<0:
        neg.append(i)
        negative_total+=i
negative_average=negative_total/len(neg)
print(f"the average of given negative number is {negative_average}")




