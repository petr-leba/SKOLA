slovo = input("Zadej slovo/větu bez diakritiky s velkými písmeny: ")
slovo = slovo.upper()

posun = 3

seznam_pred = []
seznam_po = []
seznam_p_po = []

for i in range (len(slovo)):
    cislo = 0
    nove_cislo = 0

    cislo = ord(slovo[i])
    seznam_pred.append(cislo)

    nove_cislo = cislo + posun

    if nove_cislo > 90:
        nove_cislo = nove_cislo - 90 + 64
    if nove_cislo == 32:
        nove_cislo = cislo + posun
    
    seznam_po.append(nove_cislo)
    znak = chr(nove_cislo)
    seznam_p_po.append(znak)

print(seznam_pred)
print(seznam_po)
print(seznam_p_po)

for c in seznam_p_po:
    print(c,end =' ')

