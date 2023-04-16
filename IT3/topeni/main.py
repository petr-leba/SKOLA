from topeni import Heating
import time
import os
heating1 = Heating("Obývací pokoj",1.0, 10)
heating2 = Heating("Kuchyň",1.0, 5)
heating3 = Heating("Koupelna",1.0, 8)
heating1.setTemperatureToHeat(24)
heating2.setTemperatureToStop(15)

while True:
    heating1.topeni(1)
    heating2.topeni(1)
    heating3.topeni(1)
    time.sleep(1)
    os.system('cls')
    