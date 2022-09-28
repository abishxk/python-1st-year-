q=input('enter a word:')
s1=[]
x=''
le=len(q)
for i in range(le+1):
    for j in range(i):
        x=''+q[j]
    s1.append(x)
print(s1)
       



