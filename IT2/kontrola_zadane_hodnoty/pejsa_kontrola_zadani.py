a = False
i = 0
while a == False:
    if i == 3:
        print("vypotřeboval jsi 3 pokusy")
        break
    else:
        b = input("zadej čislo:")
        try:
            c = int(b)
        except ValueError:
            print("nezadal jsi celé číslo")
            i = i + 1
        else:
            a = True
            print("Zadal jsi celé číslo", c)
