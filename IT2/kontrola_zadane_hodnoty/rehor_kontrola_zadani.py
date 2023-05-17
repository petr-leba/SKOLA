konvertovano = False
wrong_guesses = 0
max_wrong_guesses = 3

while konvertovano == False:
    cislo = input("zadejte číslo")
    try:
        cele_cislo = int(cislo)
    except:
        print("nezadal jste celé číslo")
        wrong_guesses += 1
    else:
        konvertovano = True

    if wrong_guesses == max_wrong_guesses:
        print(f"You lose! ")
        break