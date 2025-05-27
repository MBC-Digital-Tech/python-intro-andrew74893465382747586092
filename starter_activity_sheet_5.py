from turtle import *

## Task 1: Look at the following code and decide which picture it will generate.
# Then download it from the shared drive, then save and run it, to check.

def demo():
  pencolor("red")
  for counter in range (20):
    forward (150)
    right(100)
  done()







def hexagon(): 
    shape("turtle")
    color('orange', 'green')
    speed(0)
    for i in range(75):
        forward (200)
        right (95)
   


def petal():
   for 1 in range(5):
     begin_fill()
     color('red')
     circle(50,100)
     left(60)
     circle(50,100)
     end_fill()

     begin_fill()
     color('yellow')
     circle(50,100)
     left(60)
     circle(50,100)
     end_fill()


def triangle():
    
    for i in range(3):
      forward(200)
      right(120)
      

def trisomething():
    for i in range(8):
      triangle()
      right(45)

trisomething()