num=int(input('enter a prime number:'))
count=0
count2=0
l=[]
for i in range(1,num+1):
    if num%i==0:
        count+=1
    else:
        continue
if count>2:
    print('given input is not a prime number')
elif count<=2:
    print('given input is a prime number')
    for i in range(num+1,1000000000000000000000000000000000):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            count2+=1
            print(i)
            if count2==3:
                break
            elif count2==0:
                print(num,'is the last prime number')
            
            
