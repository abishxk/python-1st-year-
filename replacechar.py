s=input('enter a word:')
c=input('enter a char:')
n=input('enter a new char:')
for i in range(len(s)):
    if s[i]==c:
        b=i        
a=s[:b]
e=s[b+1:]
d=a+n+e
print(d)
