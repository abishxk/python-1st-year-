count=int(input('enter number of perfect numbers:'))
x=0
startvalue=int(input('enter a start value to find next 3 perfect number:'))
for i in range(startvalue,1000000000000000000000000000):
    perfectnum=0
    for j in range(1,i):
        if i%j==0:
            perfectnum+=j
    if i==perfectnum:
        x+=1
        print(perfectnum,'is a perfect number')
        if count==x:
            break
        
