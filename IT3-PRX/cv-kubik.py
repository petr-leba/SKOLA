import time
import os


class Topeni:
    temperatureToHeat = 20
    temperatureToStop = 22

    def __init__(self, capacity, outsideTemperature):
        self.heating = False
        self.temperature = outsideTemperature
        self.capacity = capacity

    def getTemperature(self):
        return self.temperature

    def setTemperatureToHeat(cls, temperature):
        cls.temperatureToHeat = temperature

    def setTemperatureToStop(cls, temperature):
        cls.temperatureToStop = temperature

    def startHeating(self):
        self.heating = True

    def stopHeating(self):
        self.heating = False

    def setOutsideTemperature(self, temperature):
        self.temperature = temperature


# vytvoření tří objektů topení
t1 = Topeni(0.8, 10)
t2 = Topeni(1, 5)
t3 = Topeni(0.7, 15)

# nekonečný cyklus topení
while True:
    now = time.strftime("%H:%M:%S")
    print("Time:", now)

    # topení 1
    if t1.getTemperature() < Topeni.temperatureToHeat:
        t1.startHeating()
    elif t1.getTemperature() > Topeni.temperatureToStop:
        t1.stopHeating()

    if t1.heating:
        t1.temperature += t1.capacity * 1
    else:
        t1.temperature -= t1.capacity * 1

    print("T1 temperature:", t1.getTemperature(), "heating:", t1.heating)

    # topení 2
    if t2.getTemperature() < Topeni.temperatureToHeat:
        t2.startHeating()
    elif t2.getTemperature() > Topeni.temperatureToStop:
        t2.stopHeating()

    if t2.heating:
        t2.temperature += t2.capacity * 1
    else:
        t2.temperature -= t2.capacity * 1

    print("T2 temperature:", t2.getTemperature(), "heating:", t2.heating)

    # topení 3
    if t3.getTemperature() < Topeni.temperatureToHeat:
        t3.startHeating()
    elif t3.getTemperature() > Topeni.temperatureToStop:
        t3.stopHeating()

    if t3.heating:
        t3.temperature += t3.capacity * 1
    else:
        t3.temperature -= t3.capacity * 1

    print("T3 temperature:", t3.getTemperature(), "heating:", t3.heating)

    time.sleep(2)  # počkat minutu, než se bude topení měnit
    os.system('cls')  # vymazání konzole
