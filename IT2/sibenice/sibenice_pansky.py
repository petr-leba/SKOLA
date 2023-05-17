import random

slova = ["klávesnice", "řeřicha", "myš", "bubák","stůl", "meloun", "mango", "pití"]


def choose_slovicko(slova):
    return random.choice(slova)


def a():
    slovicko = choose_slovicko(slova)
    hadej_pismenko = set()
    nespravne_tipy = 0
    spravne_tipy = 0
    return slovicko, hadej_pismenko, nespravne_tipy, spravne_tipy


def display_obesenec(nespravne_tipy):
    obesenec = [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ]

    if nespravne_tipy >= 1:
        obesenec[2] = " 🤯   |"

    if nespravne_tipy >= 2:
        obesenec[3] = "  |   |"

    if nespravne_tipy >= 3:
        obesenec[3] = " \|/  |"

    if nespravne_tipy >= 4:
        obesenec[3] = " \|/  |"
        obesenec[4] = "  |   |"

    if nespravne_tipy >= 5:
        obesenec[3] = " \|/  |"
        obesenec[4] = "  |   |"
        obesenec[5] = " /    |"

    if nespravne_tipy >= 6:
        obesenec[3] = " \|/  |"
        obesenec[4] = "  |   |"
        obesenec[5] = " / \  |"

    for obraz in obesenec:
        print(obraz)


def display_slovicko(slovicko, hadej_pismenko):
    zobrazene_slovo = ""
    for pismeno in slovicko:
        if pismeno in hadej_pismenko:
            zobrazene_slovo += pismeno + " "
        else:
            zobrazene_slovo += "_ "
    print(zobrazene_slovo)


def get_hadej(hadej_pismenko):
    hadej = input("hádej písmenko: ").lower()
    while hadej in hadej_pismenko:
        print("tohle písmenko už si zkoušel")
        hadej = input("hádej písmenko: ").lower()
    hadej_pismenko.add(hadej)
    return hadej


def check_hadej(slovicko, hadej):
    return hadej in slovicko


def check_pocet_uhadnutych(slovicko, hadej):
    pocet = 0
    for pismeno in slovicko:
        if pismeno == hadej:
            pocet += 1
    return pocet


def hra():
    slovicko, hadej_pismenko, nespravne_tipy, spravne_tipy = a()
    while True:
        display_obesenec(nespravne_tipy)

        display_slovicko(slovicko, hadej_pismenko)
        hadej = get_hadej(hadej_pismenko)

        pocet_uhadnutych = check_pocet_uhadnutych(slovicko, hadej)
        if pocet_uhadnutych != 0:
            print("Správně")
            spravne_tipy += pocet_uhadnutych
        else:
            print("Špatně")
            nespravne_tipy += 1
        if set(slovicko) == hadej_pismenko:
            print("Vyhrál si!")
            break
        elif spravne_tipy == len(slovicko):
            print("Vyhrál si, ale s chybou")
            break
        elif nespravne_tipy >= 6:
            print("Prohrál si a správně bylo:", slovicko,)
            break


hra()
