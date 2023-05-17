import random
x = 0

attempts = 0


slova = ["kolo", "auto", "letadlo"]

listOfGuesses = []


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


vybSlov = random.choice(slova)

hidden_word = ""

#print(vybSlov)

x =  "_"*len(vybSlov)

#print (x)


while (attempts < 6):
      print(x)
      attempt = input("Zadej slovo/písmeno ")
      if attempt == vybSlov:
          print("Uhadl jste slovo", vybSlov)
          break
      elif attempt in vybSlov:
                  print(attempt,"je ve slově")
                  listOfGuesses.append(attempt)
                  new_x = ""
                  for index, char in enumerate(vybSlov):
                        if char == attempt:
                              new_x += attempt
                        else:
                              new_x += x[index]
                  x = new_x
                  if x == vybSlov:
                        print("Uhadl jste slovo", vybSlov)
                        break            
      else:
            print("Není")
            attempts += 1    
            print("Už jste se neuhadnuly", attempts, ", Max je 6")
            print(HANGMANPICS[attempts])

if attempts == 6:
      print("Prohrali jste")

input()           


          
