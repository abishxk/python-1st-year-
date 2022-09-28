def product(d,e):
    prod=1
    for i in d:
        prod*=d[i]
    print(prod)
    


dic=eval(input('enter a dictionary'))
ele=dic.values()
product(dic,ele)
