mylist=('name1','name2','name3','city1','city2','city3')
name=(input('enter your name to check availability:'))
if name in mylist:
    print('name is available')
if name not in mylist:
    print('name is not available')
city=(input('enter you city to check availability:'))
if city in mylist:
    print('city is available')
if city not in mylist:
    print('city is not available')

