from turtle import *
a=int(input('enter drawing speed(0=max):'))
bgc=input('enter background colour:')
c=input('enter line colour:')
speed(a)
color(c)
bgcolor(bgc)
b=200
while b>0:
    left(b)
    forward(b*3)
    b=b-1
