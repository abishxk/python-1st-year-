from turtle import *

speed(0)
bgcolor('skyblue')

#grass
penup()
goto(-400,-100)
pendown()
color('limegreen')
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()
  
#left mount
penup()
goto(-400,-100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

#right mount
penup()
goto(100,-100 )
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

 #center mount
penup()
goto(-160,-100 )
pendown()
color( "gray")
begin_fill()
for i in range(3):
     forward(400)
     left(120)
end_fill()

#center ice cap
penup()
goto(-35,120)
pendown()
color('white')
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

#left ice cap
penup()
goto(-215,100)
pendown()
color('snow')
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()
 
 
#right ice cap
penup()
goto(203,80)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
right(70)
end_fill()

left(50)

#sun
penup()
goto(-320,450)
pendown()
color('yellow')
begin_fill()
circle(150)
end_fill()

 #tree trunk
def tree():
    color=('brown')
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()
#tree top
    forward(10)
    left(90)
    forward(5)

#leaves on tree
    color=('forestgreen')
    begin_fill()
    circle(25)
    end_fill()

    right(90)

#plant the first tree
penup()
goto(-25,-200)
pendown()
tree()

#plant the second tree
penup()
goto(-300,-250)
pendown()
tree()
