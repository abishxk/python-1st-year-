list1=eval(input('enter a list:'))

le=len(list1)
for i in range(le-1):
    for j in range(0,le-i-1):
        if len(list1[j])>len(list1[j+1]):
            list1[j],list1[j+1]=list1[j+1],list1[j]
        else:
            continue
print("list after sorting accorind to length of element:",list1)
