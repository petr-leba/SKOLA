seznam = []
cisla = []
cisla2 = []
cisla3 = []
a = 0
b = 0
c = 0
x = 0
y = 0
z = 0

while(True):
    cislo = input("Zadej minimálně 10 čísel")
    if cislo.isdigit():
        cislo = int(cislo)
        if(cislo > 0) :
            cisla.append(cislo)
        else:
            break
    else:
        break
    if len (cisla) > 10 :
        break
x = max(cisla)

for i in range(len(cisla)):
    if cisla[i] == x:
        cisla.remove(x)
        break
#   print (cisla)

y = max(cisla)

for a in range(len(cisla)):
    if cisla[a] == y:
        cisla.remove(y)
        break
    
z = max(cisla)

for a in range(len(cisla)):
    if cisla[b] == z:
        cisla.remove(z)
        break
    
print("Maxima jsou:", x, y, z)