from turtle import *

def ctverec(strana):
    for i in range(4):
        forward(strana)
        left(90)
ctverec(100)


def obdelnik(line):
    for x in range(2):
        forward(line * 2)
        left(90)
        forward(line)
        left(90)
obdelnik(100)

def troj(strany):
    for e in range(3):
        forward(strany)
        left(120)
troj(100)

def kruh(L):
    for o in range(360):
        forward(L)
        left(1)
kruh(1)

input()
