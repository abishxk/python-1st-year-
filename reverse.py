n=(input('enter a num'))
a=print("Is the number 1.POSITIVE or 2.NEGATIVE :")
if a ==1:
    rev=(n[::-1])
    print(rev)
elif a==2:
    rev=(n[1:len(n):-1])
    print("-",rev)

                    
