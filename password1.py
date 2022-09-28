import random
up = 'QWERTYUIOPASDFGHJKLMNBVCXZ'
low = 'qwertyuiopasdfghjklmnbvcxz'
num = '1234567890'
sym = '!@#$%&*(){}[]=+/?,.'
all = up+low+num+sym
len = 9

passw = ''.join(random.sample(all,len))
print(passw)