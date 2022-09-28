def listcommon(l1,l2):
    a=[]
    b=[]
    for i in l1:
        if i in l2:
            a.append(i)
    for j in l2:
        if j in l1:
            b.append(j)
    if a==[]:
        print('given list has no common elements')
    elif b==[]:
        print('given list has no common elements')
    else:
        print((a,b))
l1=eval(input('enter a first list:'))
l2=eval(input('enter a second list:'))
listcommon(l1,l2)


 
