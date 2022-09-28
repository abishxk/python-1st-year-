def search(a):
    b=eval(input('enter a key'))
    if b in a:
        print('the value for the key is',a[b])
    else:
        print('key is invalid')
dict={"A":45,"B":24,"C":35,"D":44,"F":58}
search(dict)
        
