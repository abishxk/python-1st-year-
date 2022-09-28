n=input('enter a state name:')
n2=n.lower()
if ' ' in n2: ok={'tamil nadu':'TN','andhra pradesh':'ap','punjab':'pj','kerala':'kl','delhi':'d'}
else:ok={'tamilnadu':'TN','andhrapradesh':'ap','punjab':'pj','kerala':'kl','delhi':'d'}
print(ok[n2])

