n=eval(input('enter a list'))
c=0
p=0
le=len(n)
count=0
for i in n:
    for j in range(1,le):
        if i%j!=0:
            count+=1
            if count<=2:
                p+=1
c=le-p
print('num of prime',p)
print('num of composite',c)
                
                
            
