def keycheck(di,ke):
    if ke in di:
        print('the key',key,'is in the dictionary')
    else:
        print('the key',key,'is not in the dictionary')


dic=eval(input('enter a dictionary'))
key=eval(input('enter a key to seach'))
keycheck(dic,key)

