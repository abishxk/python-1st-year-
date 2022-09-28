def search(element,list1):
    count=0
    for i in range(len(list1)):
        if list1[i]==element:
            print('element',element,'is found at the position',i+1)
            count=count+1
        else:
            continue
    print('the element is found',count,'times')
    if count==0:
        print('the element',element,'is not found in the given list')
        

list1=eval(input('enter a list'))
element=eval(input('enter a element to search in the list')) 
search(element,list1)
