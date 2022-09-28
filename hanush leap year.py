year=int(input("enter a leap year:"))
count=0
if year%4==0:
    print("the given ",year,"is leap year")
elif year%4!=0:
    for i in range(year,year+5):
        if i%4==0:
            count+=1
            print("the given",year,"not a leap year",'the next leap year is',i)
            if count==1:
                break
