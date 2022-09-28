a=float(input('Enter the marks in Python:'))
b=float(input('Enter the marks C programming:'))
c=float(input('Enter the marks in Mathematics:'))
d=float(input('Enter the marks in Physics:'))
if a>100 or 0>a:
    print()
    print('invalid mark')
elif b>100 or 0>b:
    print()
    print('invalid mark')
elif c>100 or 0>c:
    print()
    print('invalid mark')
elif d>100 or 0>d:
    print()
    print('invalid mark')
else:
    x=a+b+c+d
    mark =x/4
    print()
    print('Total=',x)
    print('Aggregate=',mark)
    print()
    if mark>=75:
            print('Distinction')
    elif mark>61 and mark<75:
            print('First Division')
    elif mark>51 and mark<60:
            print('Second Divison')
    elif mark>41 and mark<50:
            print('Third Division')
    elif mark<40 and mark>=0:
            print('Fail')

            




