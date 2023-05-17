import turtle
def ctverec(t, strana):
    for i in range(4):
        t.forward(strana)
        t.left(90)
ctverec(turtle,100)
def trojuhelnik(t,strana):
    for i in range(3):
        t.forward(strana)
        t.left(120)
trojuhelnik(turtle,100)
def kruh(t,strana):
    for i in range(36):
        t.forward(strana)
        t.left(10)
kruh(turtle,100)
def obdelnik(t, strana):
    for i in range(2):
        t.forward(strana)
        t.left(90)
        t.forward(strana*2)
        t.left(90)
obdelnik(turtle,100)