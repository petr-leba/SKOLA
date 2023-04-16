import time

class Topeni:
    temperatureToHeat = 22 # nastavíme teplotu, při které začneme topit
    temperatureToStop = 20 # nastavíme teplotu, při které přestaneme topit
    
    def __init__(self, capacity, outsideTemperature, temperature=20):
        self.capacity = capacity
        self.temperature = temperature
        self.outsideTemperature = outsideTemperature
        self.heating = False
    
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
    
    def simulate(self):
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if self.heating:
                self.temperature = self.temperature + self.capacity * elapsed_time / 60.0
            else:
                self.temperature = self.temperature - self.capacity * elapsed_time / 60.0
            if self.temperature >= self.temperatureToHeat:
                self.startHeating()
            elif self.temperature <= self.temperatureToStop:
                self.stopHeating()
            print(f"Current temperature: {self.temperature:.1f}°C | Heating: {self.heating} | Outside temperature: {self.outsideTemperature}°C")
            time.sleep(1)
            
# vytvoříme tři objekty topení pro tři různé místnosti
topeni1 = Topeni(0.8, 10)
topeni2 = Topeni(0.9, 15)
topeni3 = Topeni(1.0, 20)

# nastavíme počáteční teploty pro každou místnost
topeni1.temperature = 15
topeni2.temperature = 18
topeni3.temperature = 22

# spustíme simulaci pro každou místnost
start_time = time.time()
print("Simulating heating system...")
topeni1.simulate()
topeni2.simulate()
topeni3.simulate()
