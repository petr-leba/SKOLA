konvertovano = False
pocet_pokusu = 0

while konvertovano == False:
    if pocet_pokusu < 3:
        cislo = input("Zadejte čislo: ")
        pocet_pokusu = pocet_pokusu + 1
        try:
            cele_cislo = int(cislo) 
        except:
            print("Nezadal jste celé číslo")
        else:
            konvertovano = True
    else:
        print("Nezadal jste 3x po sobě číslo, prosím zkuste to později.")
        exit(1)

print("Zadal jste číslo", cele_cislo, "konvertování proběhlo v pořádku.")
