import turtle

def trojuhelnik(t, strana):
    for i in range(3):
        t.forward(strana)
        t.left(120)

trojuhelnik(turtle, 100)

def trojuhelnik(t, strana):
    for i in range(3):
        t.forward(strana)
        t.left(120)

trojuhelnik(turtle, 100)

def kruh(t, polomer):
    t.circle(polomer)

kruh(turtle, 100)

def obdelnik(t, strana1, strana2):
    for i in range(2):
        t.forward(strana1)
        t.left(90)
        t.forward(strana2)
        t.left(90)

obdelnik(turtle, 100,50)