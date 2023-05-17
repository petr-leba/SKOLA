veta=input("Zadejte větu velkými písmeny a bez diakritiky: ")
veta=veta.upper()

posun=3

seznam=[]
seznam_po=[]
seznam_p_po=[]

for i in range(len(veta)):
    cislo=0
    nove_cislo=0

    cislo=ord(veta[i])
    seznam.append(chr(ord(veta[i])+posun))
    nove_cislo=cislo+posun
    if nove_cislo >90:
        nove_cislo=nove_cislo -90+64
    seznam_po.append(nove_cislo)
    znak=chr(nove_cislo)
    seznam_p_po.append(znak)
print("Zadal jste větu: ",veta)
print("Vaše šifra je: ") 
for seznam_p_po in seznam_p_po:
    print(seznam_p_po, end=" ")
