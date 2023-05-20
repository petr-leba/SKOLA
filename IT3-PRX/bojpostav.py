class Misto:
    def __init__(self, jmeno, popis, okoli):
        self.jmeno = jmeno
        self.popis = popis
        self.okoli = okoli

class Postava:
    def __init__(self, jmeno, popis, stav, misto):
        self.jmeno = jmeno
        self.popis = popis
        self.stav = stav
        self.misto = misto

misto1 = Misto("Domov", "Toto je tvůj domov", {"north": None, "south": None, "west": None, "east": "misto2"})
misto2 = Misto("Les", "Nacházíš se v hustém lese", {"north": None, "south": None, "west": "misto1", "east": "misto3"})
misto3 = Misto("Jezero", "Před tebou se rozkládá jezero", {"north": None, "south": None, "west": "misto2", "east": None})

postava = Postava("Jana", "Mladá dobrodružka", misto1, misto1)

print("Jsi v", postava.misto.jmeno, "-", postava.misto.popis)

while True:
    prikaz = input("Kam se chceš vydat? north/south/west/east/exit\n")

    if prikaz == "exit":
        print("Opouštíš svět...")
        break

    if prikaz not in postava.misto.okoli:
        print("Tady se tam nedá jít.")
        continue

    dalsi_misto = postava.misto.okoli[prikaz]

    if dalsi_misto is None:
        print("Tady nelze jít.")
    else:
        postava.misto = dalsi_misto
        print("Jsi nyní v", postava.misto.jmeno, "-", postava.misto.popis)
