import time

class Room:
    def __init__(self, name, heating_power):
        self.name = name
        self.heating_power = heating_power
        self.temperature = 20
        self.is_heating = True
    
    def heat_up(self):
        while self.is_heating:
            if self.temperature < 25:
                self.temperature += 0.5 
                print(f"{self.name} is now {self.temperature} degrees Celsius.")
                time.sleep(2)
            else:
                print(f"Heating in {self.name} has stopped.")
                self.is_heating = False
                self.cool_down()

    def cool_down(self):
        while self.temperature > 20:
            self.temperature -= 0.5
            print(f"{self.name} is now {self.temperature} degrees Celsius.")
            time.sleep(2)

room1 = Room("Living room", 2)
room2 = Room("Bedroom", 2)
room3 = Room("Kitchen", 2)

room1.heat_up()
room2.heat_up()
room3.heat_up()