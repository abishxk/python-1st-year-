list1=eval(input('enter a list'))
list2=eval(input('enter another list'))

list3=list1+list2

print(f'list after merging {list3}')
le=len(list3)
for i in range(le):
    for j in range(0,le-1):
        if list3[j]>list3[j+1]:
            list3[j],list3[j+1]=list3[j+1],list3[j]
        else:
            continue
print('list after sorting:',list3)
