znamky = []
soucet = 0

while True: 
    znamka = int(input("Zadejte znamku: "))
    if znamka == 27:
        break
    soucet = soucet + znamka
    znamky.append(znamka)

print(znamky)
print(soucet)
prumer = soucet / len(znamky)
print(prumer)
