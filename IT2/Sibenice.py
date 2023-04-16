import random
word = "e"
entry = ""
game = 1
level = 0
wordinput = ("")
charactersknown = [
    
]
wrongcharacters = [

]
words = [
    'apple', 'banana', 'cherry', 'dog', 'elephant', 'flower', 'guitar', 'happy',
    'igloo', 'jacket', 'kite', 'lemon', 'monkey', 'ninja', 'orange', 'pizza',
    'queen', 'rainbow', 'sunset', 'tiger', 'unicorn', 'violet', 'water',
    'xylophone', 'yellow', 'zebra', 'basket', 'camera', 'dragon', 'eagle',
    'fossil', 'giraffe', 'hammer', 'island', 'jungle', 'kangaroo', 'lizard',
    'mango', 'noodle', 'octopus', 'pencil', 'quilt', 'rocket', 'scissors',
    'turtle', 'umbrella', 'vase', 'waffle', 'xylophone', 'yogurt', 'zeppelin',
    'abacus', 'butterfly', 'carousel', 'dolphin', 'eclipse', 'firefly',
    'gazelle', 'hurricane', 'iguana', 'jigsaw', 'kangaroo', 'lighthouse',
    'mushroom', 'nucleus', 'ostrich', 'parrot', 'quicksand', 'rhinoceros',
    'seagull', 'toucan', 'umbrella', 'volcano', 'whale', 'candy', 'yacht',
    'zealous', 'anemone', 'bluebird', 'caterpillar', 'dandelion', 'earring',
    'flamingo', 'goldfish', 'hedgehog', 'iceberg', 'jackfruit', 'kangaroo',
    'llama', 'mermaid', 'nightingale', 'ocean', 'pineapple', 'quetzal',
    'raspberry', 'sunflower', 'tangerine', 'unicorn', 'vampire', 'walrus',
    'xenophobia', 'yellowstone', 'zebrafish'
        ]

def PickWord():
    global word
    word = random.choice(words)



def Draw():
    done = 0
    global game
    global word
    global charactersknown
    global wrongcharacters
    global words
    global entry
    game = 1
    global level
    if level == 0:
        print("")
        print("")
        print("")
        print("")
        print("")
    elif level == 1:
        print("")
        print("")
        print("")
        print("")
        print("/-\\")
    elif level == 2:
        print("")
        print(" I ")
        print(" I ")
        print(" I ")
        print("/-\\")
    elif level == 3:
        print(" _ _ _ _ _")
        print(" I       ")
        print(" I      ")
        print(" I       ")
        print("/-\\")
    elif level == 4:
        print(" _ _ _ _ _")
        print(" I       O")
        print(" I      ")
        print(" I       ")
        print("/-\\")
    elif level == 5:
        print(" _ _ _ _ _")
        print(" I       O")
        print(" I      /I\\")
        print(" I       ")
        print("/-\\")
    elif level == 6:
        print(" _ _ _ _ _")
        print(" I       O")
        print(" I      /I\\")
        print(" I       n")
        print("/-\\")
    else:
        print("You lost! The word was "+word.upper()+".")
        game = 0
    print("")
    if game == 1:
        global entry
        entry = ""
        for x in word:
            if x in charactersknown:
                entry = entry+x.upper()+" "
            else:
                entry = entry+"_ "
        print(entry)
        print("")
        if not "_" in entry:
            for a in range(10):
                print("")
            print("")
            print("____   ____.__        __                       ._.")
            print("\   \ /   /|__| _____/  |_  ___________ ___.__.| |")
            print(" \   Y   / |  |/ ___\   __\/  _ \_  __ <   |  || |")
            print("  \     /  |  \  \___|  | (  <_> )  | \/\___  | \|")
            print("   \___/   |__|\___  >__|  \____/|__|   / ____| __")
            print("                   \/                   \/      \/")
            print("")
            print("")
            game = 0
    if game == 1:
     while done == 0:
        wordinput = input("Guess a character: ")
        wordinput = wordinput.lower()
        if len(wordinput) == 1 and wordinput.lower() in "abcdefghijklmnopqrstuvwxyz":
            done = 1
     if wordinput in word:
         charactersknown.append(wordinput)
         Draw()
     else:
        if not wordinput.lower() in wrongcharacters:
            level = level+1
            wrongcharacters.append(wordinput.lower())
        Draw()
    if game == 0:
        print("")
        playagain = input("Want to play again?(y/n) ")
        if playagain.lower() == "y" or playagain.lower() == "yes":
            entry = ""
            game = 1
            level = 0
            wordinput = ("")
            charactersknown = [

            ]   
            wrongcharacters = [   

            ]
            PickWord()
            Draw()
        else:
            quit()


    

    




PickWord()

Draw()



"""
wordinput = input("Hádejte písmeno: ")
wordinput = wordinput.lower()
if len(wordinput) == 1 and wordinput.lower() in "abcdefghijklmnopqrstuvwxyz":
print(wordinput)
"""       



"""
print(" _ _ _ _ _")
print(" I       O")
print(" I      /I\\")
print(" I       n")
print("/-\\")
"""