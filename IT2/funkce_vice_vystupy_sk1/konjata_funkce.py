def serad_parametry(a, b, c):
    seznam = [a, b, c]
    seznam.sort()
    a, b, c = seznam[0], seznam[1], seznam[2]
    return a, b, c

parametr1 = 5
parametr2 = 2
parametr3 = 7

parametr1, parametr2, parametr3 = serad_parametry(parametr1, parametr2, parametr3)

print(parametr1, parametr2, parametr3)