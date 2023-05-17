konvertovano = False

kolo = 0
konec = 3

while konvertovano == False:
    cislo = input("Zadejte číslo")
    try:
        cele_cislo = int(cislo)  # převod na číslo
    except ValueError:
        kolo += 1
        print("Nezadal jste celé číslo")
        if kolo == konec:
            print("Nedokázal si zadat celé číslo třikrát za sebou. Gratulace idiote!!!")
    else:
        konvertovano = True

print("Zadal jste číslo", cele_cislo)