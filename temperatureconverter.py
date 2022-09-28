def temperature():
    ch=(input('''choose an option:
    1.celsius to fahreheit
    2.fahrenheit to celsius
    >>'''))
    if ch=='1':
        temp=int(input('enter the temperature in celsius:'))
        fahrenheit=(temp*1.8)+32
        print('the given temperature is in farhrenheit is',fahrenheit)
    elif ch=='2':
        temp=int(input('enter the temperature in fahrenheit:'))
        celsius=(temp-32)*5/9
        print('the given temperature is in celsius is',celsius)
    else:
        print('invalid input')
        temperature()

temperature()
