import time


class Heating:

    temperatureToHeat = 17
    temperatureToStop = 22
    centralHeatingOn = True
    outdoorTemperature = 10

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
        self.heating = True

    def stopHeating(self):
        self.heating = False

    def setOutsideTemperature(self, temperature):
        self.outdoorTemperature = temperature

    def simulate(self):
        lastTime = time.time()
        while True:
            currentTime = time.time()
            elapsedTime = currentTime - lastTime

            if self.centralHeatingOn:
                if self.heating:
                    self.temperature = self.temperature + self.capacity * elapsedTime
                    if self.temperature >= self.temperatureToHeat:
                        self.stopHeating()
                else:
                    self.temperature = self.temperature - self.capacity * elapsedTime
                    if self.temperature <= self.temperatureToStop:
                        self.startHeating()

                if self.temperature > self.temperatureToStop and not self.heating:
                    self.temperature = self.temperatureToStop

                if self.temperature < self.temperatureToHeat and self.heating:
                    self.temperature = self.temperatureToHeat

            else:
                if self.temperature > self.outdoorTemperature:
                    self.temperature = max(self.outdoorTemperature, self.temperature - self.capacity * elapsedTime)
                elif self.temperature < self.outdoorTemperature:
                    self.temperature = min(self.outdoorTemperature, self.temperature + self.capacity * elapsedTime)

            print("Heating:", self.name, "Temperature:", self.temperature, "Heating Status:", self.heating)

            lastTime = currentTime

    @classmethod
    def turnCentralHeatingOn(cls):
        cls.centralHeatingOn = True

    @classmethod
    def turnCentralHeatingOff(cls):
        cls.centralHeatingOn = False

    @classmethod
    def setOutdoorTemperature(cls, temperature):
        cls.outdoorTemperature = temperature

    @staticmethod
    def listHeaterStatus(heater):
        print("Heating:", heater.name, "Heating Status:", heater.heating)


room1 = Heating(0.7, 1, "Room 1")
room1.setTemperatureToHeat(18)
room1.setTemperatureToStop(21)
room1.startHeating()

room2 = Heating(3, 8, "Room 2")
room2.setTemperatureToHeat(20)
room2.setTemperatureToStop(23)
room2.startHeating()

room3 = Heating(0.3, 22, "Room 3")
room3.setTemperatureToHeat(17)
room3.setTemperatureToStop(20)
room3.startHeating()

Heating.turnCentralHeatingOff()
Heating.setOutdoorTemperature(5)
Heating.listHeaterStatus(room1)
