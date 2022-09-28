a=input('enter a string:')
b=input('enter a character to search:')
if b in a:
    for i in range(len(a)):
        if a[i]==b:
            print('the character is persent at the index ', i)
else:
    print('the given character is not present in the string') 
