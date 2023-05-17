veta= input("Zadej větu bez diakritiky a napište je velkými písmenemy: ")
veta= veta.upper()
print(veta)
posun= 5
seznam_pred= []
seznam_po= []
seznam_p_po= []
sifra=""
for i in range(len(veta)):
    cislo= 0
    nove_cislo= 0
    
    cislo=ord(veta[i])
    seznam_pred.append(cislo)
    
    nove_cislo= cislo+posun
    
    if cislo != 32:
        nove_cislo=cislo + posun
    else:
        nove_cislo=cislo
    
    if nove_cislo > 90:
        nove_cislo= nove_cislo -90 + 64
    seznam_po.append(nove_cislo)
    znak= chr(nove_cislo)
    seznam_p_po.append(znak)

print(seznam_pred)
print(seznam_po)
print(seznam_p_po)