konvertovano = False
pocet_pokusu = 0

while konvertovano == False: 
    if pocet_pokusu == 3:
        print("Nezadal jste 3x po sobě číslo, prosím zkuste to později.")
        exit(1)
    else:
        cislo = input("Zadejte číslo: ")
        pocet_pokusu = pocet_pokusu + 1 
        try:
            cele_cislo = int(cislo)
        except:
            print("Není to číslo.")
        else:
            konvertovano = True

print("Zadal jste číslo", cele_cislo, "konvertování proběhlo v pořádku.")