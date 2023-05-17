def serad_parametry (a, b, c):
    seznam = [a, b, c]
    seznam.sort()
    a, b, c, = seznam
    return a,b,c
a = int(input("vlož číslo"))
b = int(input("vlož číslo"))
c = int(input("vlož číslo"))
a,b,c= serad_parametry(a,b,c)
print(a,b,c)