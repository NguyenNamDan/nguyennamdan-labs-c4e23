from turtle import *
speed(0)
color('blue')
def draw_star(x, y, length):
    penup()
    setx(x)
    sety(y) 
    pendown()
    for i in range(5):
        forward(length) 
        right(144)
# draw_star(0, 1, 100) 
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop() 