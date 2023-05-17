import random
import os

# Seznam slov pro hru
slova = ["pes", "kočka", "ryba", "pták", "slon", "lev", "krokodýl", "panda", "hroch", "žirafa"]

while True:
    # Náhodný výběr slova ze seznamu
    slovo = random.choice(slova)

    # Počet chyb hráče
    pocet_chyb = 0

    # Seznam hádaných písmen
    hodnoty = ["_" for pismeno in slovo]

    # Funkce pro vykreslení šibenice
    def vykresli_sibenici(pocet_chyb):
        obrazek = [
            "  ____",
            "  |  |",
            "  |  " + ("O" if pocet_chyb > 0 else ""),
            "  | " + ("\\|" if pocet_chyb > 1 else " "),
            "  | " + ("/ \\" if pocet_chyb > 2 else ("/" if pocet_chyb > 1 else "")),
            "__|__"
        ]
        for radek in obrazek:
            print(radek)

    while True:
        # Překreslení obrazovky
        os.system("cls" if os.name == "nt" else "clear")

        # Vykreslení šibenice
        vykresli_sibenici(pocet_chyb)

        # Vypsání aktuálního stavu hádaného slova
        print(" ".join(hodnoty))

        # Kontrola, zda hráč uhodl celé slovo
        if "_" not in hodnoty:
            print("Gratuluji, uhodl jsi slovo '{}'!".format(slovo))
            break

        # Ptání se na písmeno
        hadane_pismeno = input("Uhodni písmeno: ").lower()

        # Kontrola, zda písmeno je v hádaném slově
        if hadane_pismeno in slovo:
            for i in range(len(slovo)):
                if slovo[i] == hadane_pismeno:
                    hodnoty[i] = hadane_pismeno
        else:
            pocet_chyb += 1

        # Kontrola, zda hráč prohrál
        if pocet_chyb == 3:
            # Vykreslení šibenice
            os.system("cls" if os.name == "nt" else "clear")
            vykresli_sibenici(pocet_chyb)

            # Oznámení prohry
            print("Prohrál jsi, hádané slovo bylo '{}'.".format(slovo))
            break

