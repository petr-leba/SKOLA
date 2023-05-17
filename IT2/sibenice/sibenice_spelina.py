import random
import string

slova = ["kralik","kocka","velbloud","dromedar","ovce","slepice"]
slovo = random.choice(slova) 
spravne = ["_"]*len(slovo)
spatne = []
kontrola = False
sibenice = ["\n|\n|\n|\n|", "_____\n|\n|\n|\n|", "_____\n|    |\n|\n|\n|", "_____\n|    |\n|   \O/\n|\n|", "_____\n|    |\n|   \O/\n|    |\n|","_____\n|    |\n|   \O/\n|    |\n|   / \ "]
seznam = 0
pismeno = input("Zadej pismeno")
while kontrola == False: 
#    pismeno = input("Zadej pismeno") 
    if pismeno in string.ascii_lowercase and len(pismeno)==1: 
        if pismeno in slovo:
            
            for i in range(len(slovo)):
                if slovo[i]==pismeno:
                    spravne[i]=pismeno
            print (pismeno)
        else:
            if pismeno in spatne:
                print ("Pismeno se opakuje")
            else:
                print ("Pismeno zde neni")
                spatne.append(pismeno)
                seznam = seznam + 1
        kontrola = True
        for spravnepismeno in spravne:
            if spravnepismeno == "_":
                kontrola = False
                break   
        if len(spatne)==6:
            print ("Prohra")
        #   print(sibenice[5])
        #   print ("_____")
        #   print ("|    |")
        #   print ("|   \O/")
        #   print ("|    |")
        #   print ("|   / \")
            kontrola = False
            break 
            
        print (" ".join(spravne))
        print (" ".join(spatne))
        print (sibenice[seznam])   
        
    else:
        print ("Pouze jedno pismeno")
    pismeno = input("Zadej pismeno")
if kontrola == True:
    print ("Viteztvi")