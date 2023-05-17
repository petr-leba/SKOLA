import random

slova_tajna = ["rajtora","jirka","pepa","bobe","lavice","jednorozec"]
slovo =random.choice(slova_tajna)
delka = len(slovo)
print("začínáme")

count = 0
display = '*' * delka
limit = 9

def panak(count, display, slovo, limit):
    
    uhodni = input("tohle je to slovo:   " + display + "   ykus pismena:   ")
    if uhodni in slovo:
        index = slovo.find(uhodni)
        slovo = slovo[:index] + "*" + slovo[index + 1:]
        display = display[:display] + uhodni + display[display + 1:]
        print(display)
    else:
        count+- 1
        if count == 1:
            print("spatně ", + str(limit - count) + "zkus znova" )
           

            print("═╩═  \n"  
            )  
        elif count == 2:
            print("spatně", + str(limit - count) + "zkus znova" )
            
            print(" ╔ \n"
                  " ║   \n"  
                  " ║    \n"
                  "═╩═   \n" 
            )
        elif count == 3:
            print("spatně", + str(limit - count) + "zkus znova" )
            
            print("╔═════╗  \n"
                  "║     \n"
                  "║    \n"
                 "═╩═    \n"
            )
        elif count == 4:
            print("spatně", + str(limit - count) + "zkus znova" )
            

            print(" ╔═════╗  \n"
                  " ║     ☻  \n" 
                  " ║    \n"
                 " ═╩═     \n"     
            )
        elif count == 5:
            print("spatně", + str(limit - count) + "zkus znova" )

            print(" ╔═════╗ \n"
                  " ║     ☻  \n"
                  " ║     |  \n"
                 " ═╩═      \n"
            )
        elif count == 6:
            print("spatně", + str(limit - count) + "zkus znova" )
            print(" ╔═════╗  \n"
                  " ║     ☻  \n"
                  " ║    /|  \n"
                 " ═╩═     \n"
            )
        elif count == 7:
            print("spatně", + str(limit - count) + "zkus znova" )
            
            print(" ╔═════╗  \n"
                  " ║     ☻   \n"
                  " ║    /|\  \n"
                  "═╩═       \n"
            )
        elif count == 8:
            print("spatně", + str(limit - count) + "zkus znova" )
            print(" ╔═════╗   \n"
                  " ║     ☻    \n"
                  " ║    /|\   \n"
                  "═╩═   /      \n"
            )
        elif count == 9:
            print("spatně prohral si" )

            print(" ╔═════╗  \n"
                  " ║     ☻   \n"
                  " ║    /|\   \n"
                  "═╩═   / \   \n"
            )

if slovo == '*' * delka:
    print("gratulace pepiku")
elif count != limit:
    panak(count, display, slovo, limit)


panak(count, display, slovo)
