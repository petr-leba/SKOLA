import random

x = 0

sibenice = [ """ 
____
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
__  __    __    _   _  __       _       
| \ | \  /  \   |   |  | \     / \      
| / | / |    |  |___|  | /    /   \     
|   |\  |    |  |   |  |\    /_____\    
|   | \  \__/   |   |  | \  /       \   
"""
]

slova = ["odčinitelný", "podvedenou", "lyonské", "dosahovaným", "nezašprcla", "třicetiletého", "zabývám", "sebepěknější", "těžkooděný", "ztělesňuješ", "přislazovaných", "nedořečenou", 'rudimentálnější', 'pivoňku', 'opatrnickému', 'cestopisech', 'zmocňujících', 'štaci', 'nejvláčnějších', 'nesponzorovaly', 'zaštěkala', 'podbíhávanými', 'udrbávané',"živého"]

slovo = random.choice(slova)

print(slovo)

print(sibenice[x])

print("hádej: " ,'_'*len(slovo))

c = '_'*len(slovo)




count = 0

count = count + 1

while count < 7:
    
    
    
    a = input("hádej písmeno nebo slovo: ")

   

    if(a == slovo):
        print("vyhrál jsi")
    elif a in slovo:
     print(sibenice[x])
     b = slovo.find(a) 
     
     c = c[:b] + a + c[b+1:]
     print(c)
    else:
        print("špatně")
        x += 1 
        print(sibenice[x])
        print(c)

print("prohráli jste")

