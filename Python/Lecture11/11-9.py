import random
import turtle 
t=turtle.Turtle()
t.shape('turtle')
def left():
    t.left(30)
    t.forward(10)
def right():
    t.right(30)
    t.forward(10)
screen=t.getscreen()

def up():
    t.forward(10)
def down():
    t.backward(10)

screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")