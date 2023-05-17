konvertovano = False
fail = 0

while konvertovano == False:
    cislo = input("Zadejte čislo")
    try:
        cislo = int(cislo) #prevede na cislo
    except:
        if fail == 3:
            print("Ty magore neumíš to")
            exit(1)
        else:
            print("Nezadal jste cele číslo")
            fail += 1
    else:
        konvertovano = True
        print("Číslo je převedeno")
