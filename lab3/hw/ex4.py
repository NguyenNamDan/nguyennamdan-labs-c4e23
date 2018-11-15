from turtle import *
speed(0) 
def draw_square(l, c):
    pencolor(c)
    for i in range(4):
        forward(l)
        left(90) 
for i in range(30): 
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown() 

mainloop() 