znamky = []
soucet = 0

while True:
    znamka =int(input("Zadej ynamku:"))
    if znamka == 0:
        break
    soucet = soucet + znamka
    znamky.append(znamka)

print(znamky)
print(soucet)
prumer = soucet / len(znamky)
print(prumer)
