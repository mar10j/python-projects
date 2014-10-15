from turtle import Turtle
from random import random
    

#What I am porting from code.org


muddy = Turtle()
muddy.pensize(7)


def random_color():
    return(random(),random(),random())

while True:
    for count in range(4):
        muddy.pencolor(random_color())
        muddy.forward(1)
        muddy.right(1)
    
