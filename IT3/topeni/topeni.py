class Heating:

    #proměnné
    temperatureToHeat = 0
    temperatureToStop = 0

    def __init__(self, jmeno, capacity, outsideTemperature):
        self.jmeno=jmeno
        self.capacity = capacity
        self.outsideTemperature = outsideTemperature
        self.temperature = outsideTemperature
        self.heating = False
        self.kotel= False

    #vnitřní teplota
    @classmethod
    def getTemperature(cls):
        return cls.temperature

    #kdy začít topit
    @classmethod
    def setTemperatureToHeat(cls, temperatureToHeat):
        cls.temperatureToHeat = temperatureToHeat

    #kdy přestat topit
    @classmethod
    def setTemperatureToStop(cls, temperatureToStop):
        cls.temperatureToStop = temperatureToStop

    #spuštění topení
    @classmethod
    def startHeating(cls):
        cls.heating = True

    #vypnutý topení
    @classmethod
    def stopHeating(cls):
        cls.heating = False

    #venkovní teplota
    @classmethod
    def setOutsideTemperature(cls, outsideTemperature):
        cls.outsideTemperature = outsideTemperature
    
    @staticmethod
    def radiator(logic):
        if (logic):
            return "ZAPNUTO"
        else:
            return "VYPNUTO"
            

            
        

    #cyklus vytápění
    def topeni(self, minutes):
        stav="ZAPNUTO"
        for i in range(minutes):
            if self.heating and self.kotel==True:
                self.temperature = self.temperature + self.capacity
                stav=self.radiator(True)
            else:
               if self.temperature>self.outsideTemperature:
                    self.temperature = self.temperature - self.capacity
                    stav=self.radiator(False)

            if self.temperature < self.temperatureToStop:
                self.heating = True
                self.kotel = True
            elif self.temperature > self.temperatureToHeat:
                self.heating = False
                self.kotel=False
            
            


            print(self.jmeno,"\n", "Topení je", stav,"\n", "Teplota: ", round(self.temperature,1),"°C\n")