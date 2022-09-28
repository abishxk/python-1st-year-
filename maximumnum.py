list1=eval(input('enter a list'))

l=len(list1)
for i in range(l-1):
    for j in range(0,l-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        else:
            continue
print('the maximum element in given list is',list1[-1])

