import turtle

def trojuhelnik (t, strana):
    for i in range(3):
        t.forward(strana)
        t.left(120)

trojuhelnik (turtle, 100)          