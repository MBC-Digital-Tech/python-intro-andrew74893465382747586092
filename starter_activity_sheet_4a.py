# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python


def square():
    color('orange', 'blue')
    begin_fill()
    forward (200) 
    right (90)
    forward (200) 
    right (90) 
    forward (200) 
    right (90) 
    forward (200)
    right (90)
    end_fill()
    done() 


def triangle():
    color('orange', 'blue')
    begin_fill()
    forward (200) 
    right (120)
    forward (200) 
    right (120) 
    forward (200) 
    right (120)
    end_fill()
    penup()
    right (180)
    forward (200)
    pendown()
    forward (200) 
    right (90)
    forward (200) 
    right (90) 
    forward (200) 
    right (90) 
    forward (200)
    right (90)
    end_fill()
    
def circle_inside_circle():
    color('orange', 'blue')
    begin_fill()
    circle(10)
    penup()
    setposition(0,-70)
    pendown()
    color('blue', 'orange')
    circle(90)
    end_fill()

def pentagon():
    color('orange', 'blue')
    begin_fill()
    for i in range(6):
        speed(99999)
        forward (200) 
        right (120)
        forward (200) 
        right (120) 
        forward (200) 
        right (120)
        right (60)
    end_fill()

pentagon()