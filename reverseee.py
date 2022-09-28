a=input('enter a word:')
b=''
for i in a:
    b=i+b
print(b)

a=int(input('enter a number:'))
r=0
while a>0:
    b=a%10
    r=r*10+b
    a=a//10
print(r)
