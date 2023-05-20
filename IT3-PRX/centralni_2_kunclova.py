import time


class Heating:

    temperatureToHeat = 17
    temperatureToStop = 22

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

    def simulate(self, kdo):
        lastTime = time.time()
        while True:
            currentTime = time.time()
            elapsedTime = currentTime - lastTime

            if self.heating:
                self.temperature = self.temperature + self.capacity * elapsedTime
                if self.temperature >= self.temperatureToHeat:
                    self.heating = False

            else:
                self.temperature = self.temperature - self.capacity * elapsedTime
                if self.temperature <= self.temperatureToStop:
                    self.heating = True

            print("Temperature:", kdo, self.temperature, "Heating:", self.heating)

            lastTime = currentTime
            time.sleep(1)


room1 = Heating(0.7, 1)
room2 = Heating(3, 8)
room3 = Heating(0.3, 22)

room1.startHeating()
room2.startHeating()
room3.startHeating()

room1.simulate("1. pokoj")
room2.simulate("2. pokoj")
room3.simulate("3. pokoj")
