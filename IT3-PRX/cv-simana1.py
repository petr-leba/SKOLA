import time


class Topeni:
    temperatureToHeat = 20  # nastavení teploty, při které se topení zapne
    temperatureToStop = 22  # nastavení teploty, při které se topení vypne
    centralHeatingOn = False  # centrální topení vypnuté
    outdoorTemperature = 10  # výchozí venkovní teplota

    def __init__(self, capacity, outsideTemperature, name):
        self.heating = False
        self.temperature = outsideTemperature
        self.capacity = capacity
        self.name = name

    def getTemperature(self):
        return self.temperature

    def setTemperatureToHeat(self, temperature):
        self.temperatureToHeat = temperature

    def setTemperatureToStop(self, temperature):
        self.temperatureToStop = temperature

    def startHeating(self):
        if Topeni.centralHeatingOn:
            self.heating = True

    def stopHeating(self):
        self.heating = False

    def setOutsideTemperature(self, temperature):
        Topeni.outdoorTemperature = temperature

    @staticmethod
    def printHeatingStatus():
        for topeni in [topeni1, topeni2, topeni3]:
            print(f"Topení {topeni.name}: {'zapnuto' if topeni.heating else 'vypnuto'}")

    @classmethod
    def turnOnCentralHeating(cls):
        cls.centralHeatingOn = True

    @classmethod
    def turnOffCentralHeating(cls):
        cls.centralHeatingOn = False

    @classmethod
    def setOutdoorTemperature(cls, temperature):
        cls.outdoorTemperature = temperature