n=eval(input("enter a list:"))
le=len(n)
for i in range(0,le):
    for j in range(i+1,le):
        if n[j]<n[i]:
            d=n[i]
            n[i]=n[j]
            n[j]=d
print(n)
