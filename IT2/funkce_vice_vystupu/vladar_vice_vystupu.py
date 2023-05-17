def uzkupit_cisla(a,b,c):
    cisla = [a, b, c]
    cisla.sort()
    return cisla

cislo1 = int(input("Vložte první číslo:"))
cislo2 = int(input("Vložte druhé číslo:"))
cislo3 = int(input("Vložte třetí číslo:"))

uzkupeni = uzkupit_cisla(cislo1, cislo2, cislo3)

print(uzkupeni)

