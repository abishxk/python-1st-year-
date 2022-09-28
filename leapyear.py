def hans(year):
    if year%4==0:
        print('the year',year,'is a leap year')
    elif year%4!=0:
        for i in range(year,year+5):
            if i%4==0:
                print('the given year is not a leap year. the next leap year is',i)

year=int(input('enter a year:'))
hans(year)
