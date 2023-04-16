
slovoZadani = input("Zadejte slovo na hádání: ")
slovoHadani = []
slovoKryti = []
uhodnuto = 0
chyba = False
vyhra = False
stav = ""
pocetChyb = 0

slovoHadani.extend(slovoZadani)

i = 0
while (i < len(slovoZadani)):
    slovoKryti.append("_")
    i += 1
    
while(vyhra != True):
    print(stav)
    
    i = 0
    while (i < len(slovoZadani)):
        print(slovoKryti[i], end = " ")
        i += 1

    print("")
    
    odhad = str(input("Zadej písmenko: "))
    chyba = True
    i = 0
    if (odhad == slovoZadani):
        print("Vyhrál jsi!")
        vyhra = True
    
    while (i < len(slovoZadani)):
        if (slovoHadani[i] == odhad):
            slovoKryti[i] = odhad
            uhodnuto += 1
            chyba = False
        i += 1

    if (chyba):
        pocetChyb += 1
        
        if (pocetChyb == 1):
            stav = "_____"
        elif (pocetChyb == 2):
            stav =          """
                |
                |
                |
                |
                |
                |
                |_____
                            """
        elif (pocetChyb == 3):
            stav =          """
                ________
                |
                |
                |
                |
                |
                |
                |_____
                            """
        elif (pocetChyb == 4):
            stav =          """
                ________
                |      |
                |      
                |
                |
                |
                |_____
                            """
        elif (pocetChyb == 5):
            stav =          """
                ________
                |      |
                |      O
                |
                |
                |
                |
                |_____
                            """

        elif (pocetChyb == 6):
            stav =          """
                ________
                |      |
                |      O
                |     \|/
                |
                |
                |
                |_____
                            """

        elif (pocetChyb == 7):
            stav =          """
                ________
                |      |
                |      O
                |     \|/
                |      |
                |     /|
                |
                |
                |_____
                            """
            print(stav)
            print("Prohrál jsi!")
            vyhra = True
    
    if (slovoHadani == slovoKryti):
        #vyhrál
        print(stav)
        print("Vyhrál jsi!")
        vyhra = True
