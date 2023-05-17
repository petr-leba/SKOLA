seznam = []

for x in range(10):
    cislo = int(input("Zadejte cislo: "))
    seznam.append(cislo)

for i in range(3):
    seznam.sort(reverse=True)

print(seznam[0:3])
