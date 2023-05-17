def razeni(a, b, c):
    cisla = sorted([a, b, c])
    return tuple(cisla)

a = int(input("Zadej 1. číslo: "))
b = int(input("Zadej 2. číslo: "))
c = int(input("Zadej 3. číslo: "))
d = razeni(a, b, c)
print(d)