konvertovano = False
pokusy = 3
while not konvertovano and pokusy > 0:
    cislo = input("Zadejte celé číslo: ")
    try:
        cele_cislo = int(cislo)  # převod na číslo
        konvertovano = True
    except ValueError:
        print("Nezadal/a jste celé číslo")
        pokusy -= 1
        if pokusy > 0:
            print(f"Zbývá Vám {pokusy} pokus/y.\n")
        else:
            print("Nemáte více pokusů.")
if konvertovano:
    print(f"Zadal/a jste celé číslo {cele_cislo}.")
else:
    print("Bohužel jste nezadal/a celé číslo dostatečný početkrát.")

