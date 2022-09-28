import pygame as ok
name=input('enter your window name:')
h=int(input('enter your window height:'))
w=int(input('enter your window width:'))
display=ok.display.set_mode((w,h))
ok.display.set_caption(name)
n=1
while n==1:
    for i in ok.event.get():
        print(i)

