import time

class Topenipocitadlo:
    temperatureToHeat = 20 # teplota kdy začít topit
    temperatureToStop = 22 # teplota kdy přestat topit
    heating = False
    capacity = 0.8
    
    def __init__(self, temperature, capacity):
        self.temperature = temperature
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
        self.outsideTemperature = temperature
    
    def simulateHeating(self):
        while True:
            if self.heating and self.temperature < self.temperatureToStop:
                self.temperature += self.capacity * 1 # rychlost zahřívání za minutu
                print("Topeni v místnosti s teplotou", self.temperature, "stoupá.")
            elif not self.heating and self.temperature > self.outsideTemperature:
                self.temperature -= self.capacity * 1 # rychlost ochlazování za minutu
                print("Topeni v místnosti s teplotou", self.temperature, "klesá.")
            else:
                print("Topeni v místnosti s teplotou", self.temperature, "je vypnuto.")
            time.sleep(1) # pauza pro simulaci času

topeni1 = Topenipocitadlo(16, 0.6)
topeni2 = Topenipocitadlo(20, 0.9)
topeni3 = Topenipocitadlo(22, 1.0)

topeni1.setOutsideTemperature(10)
topeni2.setOutsideTemperature(12)
topeni3.setOutsideTemperature(9)

topeni1.startHeating()
topeni2.startHeating()
topeni3.startHeating()

topeni1.simulateHeating()
topeni2.simulateHeating()
topeni3.simulateHeating()

