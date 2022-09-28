a=int(input('enter a number:'))
fsum=0
for i in range (a+1,100):
    for j in range(1,i):
        if i%j==0:
           fsum+=i
           if a==fsum:
                print(i)

    
