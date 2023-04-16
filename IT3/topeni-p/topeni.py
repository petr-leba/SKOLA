import time
import os


class CentralHeating:

    outsideTemperature = 10  # teplota venku
    central_heating = False

    def __init__(self, name, temperature, capacity, toHeat=19, toStop=23):
        self.name = name
        self.temperature = temperature  # počáteční teplota v místnosti
        self.temp_actual = temperature  # teplota, která se mění
        self.capacity = capacity  # kapacita místnosti rychlost zahřátí

        self.temperatureToHeat = toHeat  # teplota kdy začít topit
        self.temperatureToStop = toStop  # teplota kdy přestat topit

        self.heating = True  # při instanciaci se zapne topení v místnosti
        self.cas_zmeny = time.time()  # cas zmeny zapnutí, vypnutí topení
        print(f"Topení {self.name} zapnuto")

    @classmethod
    def setOutsideTemperature(cls, temperature):
        cls.outsideTemperature = temperature

    @classmethod
    def startCentralHeating(cls):
        cls.central_heating = True

    @classmethod
    def stopCentralHeating(cls):
        cls.central_heating = False

    def setTemperatureToHeat(self, temperature):
        self.temperatureToHeat = temperature

    def setTemperatureToStop(self, temperature):
        self.temperatureToStop = temperature

    def setTemp(self, temperature):
        self.temp_actual = temperature

    def getTemp(self):
        return self.temp_actual

    def getSTemp(self):
        return self.temperature

    def startHeating(self):
        self.heating = True
        self.cas_zmeny = time.time()
        self.temperature = self.temp_actual
        # print(f"Topení {self.name} zapnuto")

    def stopHeating(self):
        self.heating = False
        self.cas_zmeny = time.time()
        self.temperature = self.temp_actual
        # print(f"Topení {self.name} vypnuto")

    @staticmethod
    def switching(logic):
        if logic:
            return "ZAPNUTO"
        else:
            return "VYPNUTO"

    def regulateHeating(self):
        if self.heating and self.central_heating:
            teplota = self.getSTemp() + (time.time() - self.cas_zmeny) * self.capacity
            if teplota > self.temperatureToStop:
                teplota = self.temperatureToStop
            self.setTemp(teplota)

            print(f"Topení {self.name} \t{self.switching(self.heating)} teplota je: {round(teplota, 1)} ℃")
            if teplota >= self.temperatureToStop:
                self.stopHeating()
        else:
            teplota = self.getTemp()
            if not self.central_heating and (self.getTemp() > self.outsideTemperature):
                teplota = self.getSTemp() - (time.time() - self.cas_zmeny) * self.capacity
                if teplota < self.outsideTemperature:
                    teplota = self.outsideTemperature
                self.setTemp(teplota)

            if self.central_heating and (self.getTemp() > self.temperatureToHeat):
                teplota = self.getSTemp() - (time.time() - self.cas_zmeny) * self.capacity
                if teplota < self.temperatureToHeat:
                    teplota = self.temperatureToHeat
                self.setTemp(teplota)

            print(f"Topení {self.name} \t{self.switching(self.heating)} teplota je: {round(teplota, 1)} ℃")

            if (teplota <= self.temperatureToHeat) and self.central_heating:
                self.startHeating()


CentralHeating.setOutsideTemperature(10)
CentralHeating.startCentralHeating()

topeni1 = CentralHeating("obývák", 15, 0.6)
topeni2 = CentralHeating("kuchyně", 15, 0.9)
topeni3 = CentralHeating("ložnice", 15, 1.0)

while True:
    os.system('cls')
    topeni1.regulateHeating()
    print()
    topeni2.regulateHeating()
    print()
    topeni3.regulateHeating()
    time.sleep(1)
