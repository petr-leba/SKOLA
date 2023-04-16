import random
import time

#začatek 
a = random.randint(0, 4)
bytosti = ["kocka", "pes", "goblin", "clovek", "vila"]
b = bytosti[a]

input("Zadej cokooliv pro start ")
print(b)
print("Uhodnite z: goblin, vila, clovek, pes, kocka")

print("1 otazka: Mam 4 nohy? ")
print("2 otazka: Jsem chlupatej?")
print("3 otazka: Mam velký mozek?")
print("4 otazka: Jsem velký?")
print("5 otazka: Jsem realný?")

kocka  = ["yes", "yes", "no", "no", "yes"]
pes    = ["yes", "yes", "no", "yes", "yes"]
goblin = ["no", "no", "no", "yes", "no"]
clovek = ["no", "no", "yes", "yes", "yes"]
vila   = ["no", "no", "yes", "yes", "no"]

for i in range(5):
    #1 otazka
    c = input("Hádej nebo zadej číslo otázky: ")
    if c == b:
        print("Správně")
        time.sleep(3)
        exit()
    if b == "kocka":
        print(kocka[int(c)-1])
    if b == "pes":
        print(pes[int(c)-1])
    if b == "goblin":
        print(goblin[int(c)-1])
    if b == "clovek":
        print(clovek[int(c)-1])
    if b == "vila":
        print(vila[int(c)-1])    
    
d = input("Napis jmeno tvora ")
# konec hry
if d == b:
    print("Ano uhold jste spravně")
else:
    print("Neuhodl jste spravně")
#vysledek
#print(a and b)