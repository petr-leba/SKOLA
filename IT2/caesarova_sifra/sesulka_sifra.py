veta = input("Zadejte větu, kterou chcete zakodovat: ")
veta = veta.upper()
veta_pred = []
veta_po = []
veta_p_po = ()
x = int(input("Zadejte o kolik chcete pismena posunout: "))


for i in range (len(veta)):
    
    cislo = 0
    cislo_po = 0

    cislo = ord(veta[i])

    if cislo != 32:
        cislo_po = cislo + x
    else:
        cislo_po = cislo
    
    if cislo_po > 90:
        cislo_po = cislo_po - 26

    xddxd = chr(cislo_po)
    veta_po.append(xddxd)



for p in veta_po:
    print(p, end ="")