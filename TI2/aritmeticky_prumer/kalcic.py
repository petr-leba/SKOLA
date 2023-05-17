znamky =  []
soucet = 0

while true:
    znamka =int(input(“Zadejte znamku“))
    if znamka == 0:
        break
    soucet = soucet + znamka
    znamky.append(znamka)

print(znamky)
print(soucet)
prumer = soucet / len(znamky)
print(prumer)