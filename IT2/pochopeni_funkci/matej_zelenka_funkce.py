import turtle

def ctverec(t, strana):
            for i in range(4):
                t.forward(strana)
                t.left(90)

def troj(t, strana):
            for i in range(3):
                t.forward(strana)
                t.left(120)


def obd(t, strana):
            for i in range(2):
                t.forward(100)
                t.left(90)
                t.forward(50)
                t.left(90)

def kruh(t, strana):
            t.circle(120)



print(" a čtverec", 
      "b trojúhelník",
        "c obdélník",
        "d kruh"
    )  

a = input( "zadejte tvar: ")
      
      
      
if(a  == "a"): 

    ctverec(turtle, 100)
elif(a == "b"):

    troj(turtle,100)

elif(a == "c"):
    obd(turtle, 100)

elif(a == "d"):
    kruh(turtle, 1)