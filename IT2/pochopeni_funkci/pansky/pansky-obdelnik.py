import turtle

def obdelnik(t, strana1, strana2):
    for i in range(2):
        t.forward(strana1)
        t.left(90)
        t.forward(strana2)
        t.left(90)

obdelnik(turtle, 100, 50)
