def pismenka(a, b, c):
    # vytvoření seznamu s parametry a, b, c
    cisla = [a, b, c]
    # seřazení seznamu od nejmenšího po největší
    cisla.sort()
    # uložení seřazených hodnot zpět do původních parametrů
    a, b, c = cisla[0], cisla[1], cisla[2]
    # vrácení seřazených hodnot
    return a, b, c

a, b, c = pismenka(3, 1, 2)
print(a, b, c)  