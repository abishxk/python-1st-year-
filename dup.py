list=eval(input('enter a list:'))
le=len(list)
l2=list.copy()
n=[]
for i in list:
        if i not in n:
                n.append(i)
print(n)
