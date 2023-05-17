konvertovano = False
fail = 0

while konvertovano == False:
    cislo = (input("Zadej cislo"))
    try: 
        cislo = int(cislo)

    except:
        if fail ==3:
            print("Jseš blbej nebo co")
            exit(1)
        else:
            print("Nezadal jste celé číslo")
            fail += 1
        
    
            
    else:
            konvertovano = True
            

if cislo % 2 == 0 :
    print("Cislo je sude")

elif cislo % 2 == 1:
    print("Cislo je liche")