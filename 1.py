from turtle import *
from random import *
shape("turtle")
colormode(255)
speed(0)
pensize(5)
def random(ys,bs):
    color(ys)
    penup()
    x = randint(-300,300)
    y = randint(-300,300)
    goto(x,y)
    pendown()
    dot(bs)
    z = "("+str(x)+","+str(y)+")"
    return z
for i in range(100*10):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    bs = randint(3,9)
    z = random((r,g,b),bs)
    write(z,font = ("宋体",10))
