listt=eval(input('enter a list:'))
le=len(listt)
for i in range(1,le):
    val1=listt[i]
    j=i-1
    while j>=0 and val1<listt[j]:
        listt[j+1]=listt[j]
        listt[j]=val1
print('the list after sorting is',listt)

