def lencart(total,c,li,ca,coo,chi,co,can,a,b):
    print('Number of items in cart: ',c)
    print()
    print('items in cart :',li)
    print()
    for i in li:
        if i=='Cake':
            ca+=1
        elif i=='Candy':
            can+=1
        elif i=='Cookie':
            coo+=1
        elif i=='Chips':
            chi+=1
        elif i=='Coke':
            co+=1
        else: continue
    if 'Cake' in li:
        print('Number of CAKES in cart:',ca)
    if 'Candy' in li:
        print('Number of CANDIES in cart:',can)
    if 'Cookie' in li:
        print('Number of COOKIES in cart:',coo)
    if 'Chips' in li:
        print('Number of Chips in cart:',chi)
    if 'Coke' in li:
        print('Number of COKE in cart:',co)
    if b!=2:
        choice(total,c,li,ca,coo,chi,co,can,a)

def choice(total,c,li,ca,coo,chi,co,can,a):
     b=int(input('''Do you want to continue shopping?(1=yes/2=no/3=view cart)
    >>>'''))
     print()
     if b==1:
       shoppingcart(total,c,li,ca,coo,chi,co,can)
     elif b==2:
        print('Thank You For Shopping. Your Total is ',total)
        lencart(total,c,li,ca,coo,chi,co,can,a,b)
        a=0
     elif b==3:
        lencart(total,c,li,ca,coo,chi,co,can,a,b)
        choice(total,c,li,ca,coo,chi,co,can,a)
     else:
        print('Invalid Input... Try Again ;(')
        choice(total,c,li,ca,coo,chi,co,can,a)

def shoppingcart(total,c,li,ca,coo,chi,co,can):
    a=9
    q='Cake'
    w='Candy'
    e='Cookie'
    r='Chips'
    t='Coke'

    a=int(input('''Choose an item:
    1=Cake
    2=Candy
    3=Cookie
    4=Chip
    5=Coke
    or
    0=Quit shopping
    6=view cart
    >>'''))
    if a>0 and a<6:
        qua=int(input('Enter The Quantity Of Items:'))
    if a==1:
        print('CAKE Added To Cart :)')
        c+=qua
        total=qua*30
        for i in range(qua):
            li.append(q)
        choice(total,c,li,ca,coo,chi,co,can,a)
    elif a==2:
        print('Candy Added To Cart :)') 
        c+=qua
        total=qua*30
        for i in range(qua):
            li.append(w)
        choice(total,c,li,ca,coo,chi,co,can,a)
    elif a==3:
        print('Cookie Added To Cart :)') 
        c+=qua
        total=qua*15
        for i in range(qua):
            li.append(e)
        choice(total,c,li,ca,coo,chi,co,can,a)
    elif a==4:
        print('Chips Added To Cart :)') 
        c+=qua
        total=qua*20
        for i in range(qua):
            li.append(r)
        choice(total,c,li,ca,coo,chi,co,can,a)
    elif a==5:
        print('Coke added to cart :)') 
        c+=qua
        total=qua*25
        for i in range(qua):
            li.append(t)
        choice(total,c,li,ca,coo,chi,co,can,a)
    elif a==0:
        print('Come back soon :(')
    elif a==6:
        print('Number of items in cart: ',c)
        print('items in cart :',li)
        choice(total,c,li,ca,coo,chi,co,can,a)
    else:
        print('Invalid input... try again ;(')
        shoppingcart(total,c,li,ca,coo,chi,co,can)

        
total=0
c=0
li=[]
ca=0
coo=0
chi=0
co=0
can=0
shoppingcart(total,c,li,ca,coo,chi,co,can)
