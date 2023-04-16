"""
Jsem línej to okomentovat... 
Trvalo mi to strhujících 11 hodin na zprovoznění. Nejdříve jsem měl problém s tím, že teplota záhadně vyskočila na teplotu Slunce a pořád se zvyšovala.
Po opravě se mi objevil další problém... Tentokrát se teplota zvýšila na 13 stupňů, následně spadla na 12 stupňů a zase skočila na 13 stupňů... Tohle se pořád opakovalo.
Po zdrcujících 3 hodinách dumání jsem problém opravil. Už jsem si myslel, že to funguje, ale tentokrát jakmile teplota klesla na 5 stupňů tak tam také zůstala a nezvyšovala se.
TO SE MI TAKY PODAŘILO OPRAVIT A TO JENOM PO 2 HODINÁCH!!!!!!!! Ale zase jsem byl u problému čísla 2, neboli 12 a 13 stupňů.
Už jsem to začal vzdávat a začal brečet, že to nefunguje. Přeci jen jsem nad tím strávil už +- 6 hodin... Ale pak jsem si vzpomněl, co řekl jeden člověk: "AWDSMFAFOOTHIMAAAFOOTAFOOTWHSCUSEME." -Joe Biden
Tyto slova mě dojala a donutila k pokračování. Po dalších 2 hodinách by to už mělo fungovalo!! Teda... Myslel jsem si to... Tentokrát se teplota nezvyšovalo a zůstala zaseknutá na počáteční teplotě.
Tentokrát se u mě projevilo pět fází smutku. Nejdříve popírání, následně hněv, smlouvání, deprese a na konec smíření... V tuto chvíli jsem si dal pauzu na 2 dny. 30. a 31. března.
ALE DNES
DNES 1. DUBNA JSEM TO DOKÁZAL. Podařilo se mi zprovoznit topení a za to jsem happy jak dva grappy (šťastný jak dva grepy).
Pokud jste to dočetl až sem tak gratuluji. Doufám, že jste se alespoň pousmál nad mým trápením, nad mým dobrodružstvím a nad touto prací. Také bych chtěl dodat, že jestli to přestane fungovat tak to už neopravim. Děkuji za přečtení a pěkný zbytek dne Vám přeje: Matyáš Bárta. (a ne netuším proč jsem to sem musel napsat.)
"""


import time
import os

class Toping:
    outsideTemp = 0

    def __init__(self, name, capacity, startTemp, startHeat, stopHeat):
        self.name = name
        self.capacity = capacity
        self.startTemp = startTemp
        self.startHeat = startHeat
        self.stopHeat = stopHeat
        self.actualTemp = startTemp
        self.Heat = False
        self.kotel = False
        self.regulating = False

    @staticmethod
    def boolToSwitch(toSwitch):
        if toSwitch:
            return "ZAPNUTO"
        else:
            return "VYPNUTO"
    
    @classmethod
    def setOutsideTemp(cls, outsideTemp):
        cls.outsideTemp = outsideTemp

    @classmethod
    def startToping(cls):
        cls.Heat = True

    @classmethod
    def stopToping(cls):
        cls.Heat = False

    @classmethod
    def setStopHeat(cls, stopHeat):
        cls.stopHeat = stopHeat

    @classmethod
    def setStartHeat(cls, startHeat):
        cls.startHeat = startHeat

    def regulateHeating(self, minutes):
        stav = "ZAPNUTO" if self.Heat else "VYPNUTO"
        for i in range(minutes):
            if self.actualTemp < self.stopHeat and not self.regulating:
                self.Heat = True
                self.kotel = True
                self.regulating = True
                stav = self.boolToSwitch(True)
            elif self.actualTemp > self.startHeat and self.regulating:
                self.Heat = False
                self.kotel = False
                self.regulating = False
                stav = self.boolToSwitch(False)
            elif self.regulating:
                self.actualTemp = self.actualTemp + self.capacity
                stav = self.boolToSwitch(True)
            else:
                stav = self.boolToSwitch(False)
                self.actualTemp = self.actualTemp - self.capacity

            print(f"Topeni {self.name} je {stav} a má {self.actualTemp} °C\n")

        if self.actualTemp <= self.stopHeat:
            self.Heat = True
            self.kotel = True
            self.regulating = True
        elif self.actualTemp > self.startHeat:
            self.Heat = False
            self.kotel = False
            self.regulating = False


Toping.setOutsideTemp(13)
Toping.startToping()
heating1 = Toping("obývák", 1, 5, 12, 5)
heating2 = Toping("Pokoj", 1, 12, 24, 11)
heating3 = Toping("Ložnice", 1, 7, 21, 17)

while True:
    heating1.regulateHeating(1)
    heating2.regulateHeating(1)
    heating3.regulateHeating(1)
    time.sleep(1)
    os.system("cls")