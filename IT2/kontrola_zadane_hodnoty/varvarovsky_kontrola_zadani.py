pokus = 0
konvertovano = False

while pokus < 3 and konvertovano == False:
    cislo = input("Zadejte číslo ")
    try:
        cele_cislo = int(cislo)  # převod na číslo
    except ValueError:
        print("Nezadal jste celé číslo")
        pokus += 1
    else:
        konvertovano = True

if konvertovano == True:
    print("Zadal jste číslo")
else:
    print("Třikrát jste nezadal celé číslo")