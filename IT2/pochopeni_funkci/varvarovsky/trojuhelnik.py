import turtle

def ctverec(t, strana):
    for i in range(3):
        t.forward(strana)
        t.left(120)

ctverec(turtle, 100)