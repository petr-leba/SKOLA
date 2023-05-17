import turtle

def trojuhelnik(t, strana):
    for i in range (3):
            t.forward(strana)
            t.left(120)

trojuhelnik(turtle, 100)

def kruh(t):
    t.circle(120)
kruh(turtle)

def ctverec(t, strana):
    for i in range (4):
            t.forward(strana)
            t.left(90)

ctverec(turtle, 100)

def trojuhelnik(t):
    for i in range (2):
            t.forward(100)
            t.left(90)
            t.forward(50)
            t.left(90)

trojuhelnik(turtle)