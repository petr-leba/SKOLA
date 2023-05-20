import time
import os

class Topeni:
    temperatureToHeat = 20  # nastavení teploty, při které se topení zapne
    temperatureToStop = 22  # nastavení teploty, při které se topení vypne

    def __init__(self, capacity, outsideTemperature):
        self.heating = False
        self.temperature = outsideTemperature
        self.capacity = capacity

    def getTemperature(self):
        return self.temperature

    def setTemperatureToHeat(self, temperature):
        self.temperatureToHeat = temperature

    def setTemperatureToStop(self, temperature):
        self.temperatureToStop = temperature

    def startHeating(self):
        self.heating = True

    def stopHeating(self):
        self.heating = False

    def setOutsideTemperature(self, temperature):
        self.temperature = temperature


# vytvoření instancí topení pro tři místnosti
topeni1 = Topeni(0.8, 18)
topeni2 = Topeni(0.9, 15)
topeni3 = Topeni(1.0, 20)

while True:
    for topeni in [topeni1, topeni2, topeni3]:
        if topeni.getTemperature() < topeni.temperatureToHeat:
            topeni.startHeating()
        elif topeni.getTemperature() > topeni.temperatureToStop:
            topeni.stopHeating()

        if topeni.heating:
            topeni.temperature += topeni.capacity * 1
        else:
            topeni.temperature -= topeni.capacity * 1

        print(f"Místnost s kapacitou {topeni.capacity} a venkovní teplotou {topeni.temperature} má vnitřní teplotu {topeni.getTemperature()}")

    # time.sleep(60) # čekání jednu minutu, aby se teplota měla čas změnit
    
    time.sleep(2)
    os.system('cls')  # vymazání konzole
