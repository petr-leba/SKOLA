element = 0

veta = ""

#šifra = int(input("zadejte šifru: "))
šifra = 1

a = 0

zpráva = input("zadejte zprávu: ")

list = list(zpráva.strip(""))

while True:
    try:
        z = [list[element]]

        element = element + 1


        c = (" ".join(z))
        
        

        if(ord(c) != 32):
            if(ord(c) > 89):
                cislo = ord(c) - 26 + šifra
            else:
                cislo = ord(c) + šifra
        elif(ord(c) == 32):
            cislo = ord(c)
            
            
            


        
        veta = veta + chr(cislo)
    except:
        print("vaše šifra: ", veta )
        break

