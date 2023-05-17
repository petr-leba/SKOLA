import math

b = False

c = 1

while b == False:
    a = input("zadejte číslo: ")
    
    if(c == 3):
        print("moc pokusů na zadání čísla")
        break
    else:
    
        try:
            cle_cislo= int(a)
            b = True
        except:
            print("nezadal jste celé číslo: ")
            c = c + 1 
        else:
            print("číslo bylo konvertováno")
            b = True
