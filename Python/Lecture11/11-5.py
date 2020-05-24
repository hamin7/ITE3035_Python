import turtle

turtle.shape('turtle')

def a():
    turtle.left(30)
    turtle.fd(100)

screen = turtle.getscreen()
screen.onkeypress(a,"Up")
screen.listen()