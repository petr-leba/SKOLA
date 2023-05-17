list = []
kolo = 0

while kolo < 10:
    cislo = int(input("Vlož číslo: "))
    list.append(cislo)
    kolo += 1

top_cisla = sorted(list, reverse=True)[:3]

print("3 Největší z čísel jsou:", top_cisla)

