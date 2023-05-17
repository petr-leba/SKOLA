pocet_pokusu = 3
for i in range(pocet_pokusu):
    try:
        cele_cislo = int(input("Zadejte číslo: "))
        print("Zadal jste číslo", cele_cislo)
        break
    except ValueError:
        print("Nezadal jste celé číslo.")
else:
    print("Neumíš zadat celé číslo? ._.")

