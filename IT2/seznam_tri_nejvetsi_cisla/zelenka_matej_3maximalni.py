list = []

for x in range(10):
    cislo = int(input("zadejte cislo: "))
    list.append(cislo)

for i in range(3):
    list.sort(reverse=True)

print(list[0:3])