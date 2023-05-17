znaky = [ ]
soucet = 0

while True:
    znamka = int(input("Zadej znamku: "))
    if znamka == 0:
        break
    soucet = soucet + znamka
    znamka.append(znamka)

print(znamka)
print(soucet)
prumer = soucet / len(znamka)
print(prumer)

