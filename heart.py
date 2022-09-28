import turtle as ok
import random
a=int(random.randrange(1,255))
b=int(random.randrange(1,255))
c=int(random.randrange(1,255))
ok.bgcolor(a,b,c)
ok.pensize(5)

def curve():
    for i in range(200):
        ok.right(1)
        ok.forward(1)

ok.speed(0)
ok.color('blue','red')

ok.begin_fill()
ok.left(140)
ok.forward(111.65)
curve()

ok.left(120)
curve()
ok.forward(111.65)
ok.end_fill()
ok.hideturtle()
