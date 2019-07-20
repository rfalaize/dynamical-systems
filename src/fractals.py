# fractals

from turtle import *

setheading(90)  # the turtle points straight up
penup()         # lift the pen
setpos(0, -250) # set initial point
pendown()       # pen down

def fractal_tree_color(length, level):
    if length==0:
        return
    # draws fractal tree
    pensize(length/10)
    if length < 20:
        pencolor("green")
    else:
        pencolor("brown")
    speed(0)    # fastest speed
    if level > 0:
        fd(length)  # forward
        rt(30)      # right turn 30 degrees
        fractal_tree_color(length*0.7, level-1)
        lt(90)
        fractal_tree_color(length*0.5, level-1)
        rt(60)
        penup()
        bk(length)  # backwards
        pendown()

fractal_tree_color(200, 10)
#%%