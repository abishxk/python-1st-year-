unit=float(input('enter the unit consumed:'))

if (unit<=50):
    print('your bill is',unit*2.65)
elif (unit>=51 and unit<=100):
    print('your bill is',unit*3.35)
elif (unit>=101 and unit<=300):
    print('your bill is',unit*7.10)
else:
    print('your bill is',unit*8.50)

