def fibo():
    b,c=c,a
def fibonacci(n):
    b=0
    c=1
    for i in range(n+1):
        a=b+c
        print(b,end=' ')
        fibo()

n=int(input('enter a limit:'))
fibonacci(n)
