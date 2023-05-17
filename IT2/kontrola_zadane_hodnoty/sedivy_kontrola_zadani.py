1konvertovano = False
cislo_pocet = 0

while konvertovano == False:
    if cislo_pocet < 3:
        cilso = input("Zadej číslo: ")
        cislo_pocet = cislo_pocet + 1
        try:
            cele_cislo = int(cilso)
        except:
            print("Zkus to znova")
        else:
            konvertovano = True
    else:
        print("Neumíš to noobe :(")
        exit(1)

print("číslo je v pořádkukonvertováno :)", cele_cislo)