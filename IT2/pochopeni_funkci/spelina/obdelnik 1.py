import turtle

def obdelnik (t, a, b):
        for i in range (2):
                t.forward(a)
                t.left(90)
                t.forward(b)
                t.left(90)

obdelnik (turtle, 100, 50)        
