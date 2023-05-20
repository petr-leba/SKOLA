topeni1 = Topeni(0.8, 18, "Ložnice")
topeni2 = Topeni(0.9, 15, "Obývák")
topeni3 = Topeni(1.0, 20, "Kuchyně")

while True:
Topeni.printHeatingStatus()
Topeni.setOutdoorTemperature(15)

for topeni in [topeni1, topeni2, topeni3]:
    if not Topeni.centralHeatingOn:
        topeni.temperature -= 1
    elif topeni.getTemperature() < topeni.temperatureToHeat:
        topeni.startHeating()
    elif topeni.getTemperature() > topeni.temperatureToStop:
        topeni.stopHeating()

    if topeni.heating and topeni.getTemperature() < topeni.temperatureToStop:
        topeni.temperature += topeni.capacity * 1
    elif not topeni.heating and topeni.getTemperature() > Topeni.outdoorTemperature:
        topeni.temperature -= topeni.capacity * 1

    if topeni.getTemperature() > topeni.temperatureToStop:
        topeni.stopHeating()

    if topeni.getTemperature() < topeni.temperatureToHeat:
        topeni.startHeating()

    print(f"Místnost {topeni.name} s kapacitou {topeni.capacity} a venkovní teplotou {Topeni.outdoorTemperature} má vnitřní teplotu {topeni.getTemperature()}")

time.sleep(60) # čekání jednu minutu, aby se teplota měla čas změnit
