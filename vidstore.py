def choice():
    days=int(input('number of days you wish to rent:'))
    new=0
    old=0
    ch=int(input('''CHOOSE THE TYPE OF VIDEO:
    1.NEW
    2.OLD

    or

    3.Proceed to checkout
    >>'''))
    if ch==1:
        n=int(input('number of new videos:'))
        ok=new+((75*n)*days)
        choice()
    elif ch==2:
        o=int(input('number of old videos:'))
        ok2=old+((50*o)*days)
        choice()
    elif ch==3:
        print('Total is:',ok+ok2)
    else:
        print('enter a valid input(1,2,3)')
        choice()

choice()
