veta = input("Zadejte větu v caps locku: ")


posun = 7
sifra = ""

for i in range(len(veta)):
    a = 0
    b = 0

    a = ord(veta[i])

    if a != 32:
        b = a + posun
    else:
        b = a
        
    if b > 90:
        b = b - 26

    znak = chr(b)
    sifra += znak

print(sifra)
