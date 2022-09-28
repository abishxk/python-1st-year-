def merge(n1,n2):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    le1=len(n1)
    le2=len(n2)

    if le1>le2:
        a=n1[:le2]
        b=n1[le2:]
        for i in range(le2):
            c.append(a[i])
        for m in range(le2):
            c.append(n2[m])
        c.extend(b)   
        print(c)

    if le2>le1:
        d=n2[:le1]
        e=n2[le1:]
        for j in range(le1):
            f.append(d[j])
        for n in range(le1):
            f.append(n1[n])
        f.extend(e)   
        print(f)
    if le2==le1:
        for k in range(le1):
            g.append(n1[k])
        for o in range(le1):
            g.append(n2[o])
        print(g)
            
n1=eval(input('enter a list'))
n2=eval(input('enter a list'))
merge(n1,n2)
