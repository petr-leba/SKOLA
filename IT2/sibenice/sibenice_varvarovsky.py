import random
import os 

# Seznam slov pro hru
slova = ["pes", "kočka", "ryba", "pták", "slon", "lev", "krokodýl", "panda", "hroch", "žirafa"]

# Maximální počet pokusů
max_pokusy = 4

while True:
    # Dotaz na novou hru
    nova_hra = input("Chceš hrát hru? (ano/ne) ").lower()
    if nova_hra != "ano":
        break     
    
    # Náhodný výběr slova ze seznamu
    slovo = random.choice(slova)     
    
    # Počet chyb hráče
    pocet_chyb = 0     
    
    # Seznam hádaných písmen
    hadana_pismena = []     
    
    # Funkce pro vykreslení šibenice
    def vykresli_sibenici(pocet_chyb):
        obrazek = [
            "  ____",
            "  |  |",
            "  |  " + ("O" if pocet_chyb > 0 else ""),
            "  | " + ("/|\\" if pocet_chyb > 1 else ("|" if pocet_chyb > 0 else "")),
            "  | " + ("/ \\" if pocet_chyb > 2 else ("/" if pocet_chyb > 1 else "")),
            "__|__"
        ]
        for radek in obrazek:
            print(radek)     
    
    # Hlavní smyčka pro aktuální hru
    while pocet_chyb < max_pokusy:
        # Překreslení obrazovky
        os.system("cls" if os.name == "nt" else "clear")     
        
        # Vykreslení šibenice
        vykresli_sibenici(pocet_chyb)     
        
        # Vypsání aktuálního stavu hádaného slova
        print(" ".join([pismeno if pismeno in hadana_pismena else "_" for pismeno in slovo]))
        
        # Kontrola, zda hráč uhodl celé slovo
        if set(slovo) <= set(hadana_pismena):
            print("Gratuluji, uhodl jsi slovo '{}'!".format(slovo))
            break     
        
        # Ptání se na písmeno
        hadane_pismeno = input("Uhodni písmeno: ").lower()
        
        if len(hadane_pismeno) != 1 or not hadane_pismeno.isalpha():
            print("Zadej prosím jedno platné písmeno.")
            continue
        
        if hadane_pismeno in hadana_pismena:
            print("Toto písmeno jsi již hádal, zkus jiné.")
            continue
        
        hadana_pismena.append(hadane_pismeno)
        
        if hadane_pismeno not in slovo:
            pocet_chyb += 1
            print("Toto písmeno ve slově není")