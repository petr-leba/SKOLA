

slovo = input("Zadejte text na šifrovaní ").upper()
"""print(slovo)"""

posun = 5
seznam_pred = []
seznam_po = []
seznam_p_po = []

for i in range(len(slovo)):
    cislo = 0
    nove_cislo = 0

    cislo = ord(slovo[i])
    seznam_pred.append(cislo)

    if cislo != 32:
        nove_cislo = cislo + posun
    else:
        nove_cislo = cislo
        
    if nove_cislo > 90:
        #nove_cislo = nove_cislo - 90 + 64
        nove_cislo = nove_cislo - 26
    seznam_po.append(nove_cislo)

    znak = chr(nove_cislo)
    seznam_p_po.append(znak)



"""print(seznam_pred)
print(seznam_po)
print(seznam_p_po)"""

for p in seznam_p_po:
      print(p,end="")





