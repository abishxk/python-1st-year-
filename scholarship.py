markpercentage=int(input('enter your mark percentage:'))
age=int(input('enter your age:'))
annualincome=int(input('enter your annual income:'))

if (markpercentage>85):
    if (age<20 and annualincome<200000):
        print('you are eligible for scholarship')
    else:
        print('you are not eligible for Scholarship')
else:
    print('you are not eligible for scholarship')
