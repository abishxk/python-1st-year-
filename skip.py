M=int(input('enter a start range:'))
N=int(input('enter a end range:'))
X=int(input('enter the number of numbers to skip:'))
if M>N:
    print('invalid range')
elif N<0 or M<0:
    print('invalid range')
elif M<=X or N<=X:
    print('invalid range')
elif M==0 and N==0:
    print('invalid range')
elif X<0:
    print('invalid skip count')
elif M==N:
    print('invalid input')
else:
    for i in range(M,N+1,X):
        print(i,end=',')
