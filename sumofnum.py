def typeee():
    typee=int(input('''
enter 1 for positive value
enter 2 for negative value
>'''))


val=int(input('enter a value:'))

typee=int(input('''
enter 1 for positive value
enter 2 for negative value
>'''))
summ=0
if typee==1:
    for i in range(0,val+1):
        summ+=i
    print('the sum of given positive integer',val,'is',summ)
elif typee==2:
    for i in range(val,0):
        summ+=i
    print('the sum of given negative integer',val,'is',summ)
else:
    print('invalid input. try again :(')
    typeee()

