def fun(n):
    global a
    global b
    c=a+b
    a=b
    b=c
    print(c)
    if n!=0:
        return fun(n-1)
n=int(input("enter the range"))
a=0
b=1
c=1
print(a)
print(b)
fun(n-3)
