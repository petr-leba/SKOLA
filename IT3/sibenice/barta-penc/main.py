import random
import sibenice
hadanka=[]
with open("sibenice/barta-penc/slova.txt", "r", encoding="utf8") as file:
    slova = file.read().splitlines()

slovos = random.choice(slova)

for letter in slovos:
    hadanka.append(letter)

delka= len(slovos)
chyba=0
poprava=sibenice.obesenec[chyba]

while(chyba!= delka):

    pismeno = input("Jaké písmeno hádáš: ")
    for i in hadanka:
            
        if (i != pismeno):
           chyba=chyba+1
    print(poprava)
            
    




