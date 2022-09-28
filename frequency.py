def frequency(dic,val):
    count=0
    for i in dic:
        if dic[i]==val:
            count=+1
    print(count)

dic=eval(input('enter a dictionary'))
val=eval(input('enter a value to count'))
frequency(dic,val)
