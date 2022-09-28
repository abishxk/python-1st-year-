x=''
n=''
while n!='*':
    n=input('enter a character:')
    x+=n
upper=0
lower=0
digit=0
symbols=0
for j in range(len(x)-1):
    if x[j].isupper():
        upper+=1
    elif x[j].islower():
        lower+=1
    elif x[j].isdigit():
        digit+=1
    else:
        symbols+=1

print('symbols:',symbols)
print('upper:',upper)
print('lower:',lower)
print('digit:',digit)
        
