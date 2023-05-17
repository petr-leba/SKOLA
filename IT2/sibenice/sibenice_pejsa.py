import random
slova = ["denis", "smrt", "kral", "minecraft", "pepa", "jirka", "vrah", "kniha", "slepice", "tank", "kulka"]
podtrzitka = ["_","__","___","____","_____","______","_______","________", "_________"]
sibenice =[
""" 



|""",
""" 




|     |""",
"""   
       
     
    
         
             
|  |  |""",
"""     
        
           
          
          
             
|--|--|""",
"""      
   |       
   |         
   |       
   |       
   |          
|--|--|""",
"""  _______    
   |         
   |        
   |       
   |       
   |          
|--|--|""",
"""  _______    
   |     |    
   |         
   |       
   |       
   |          
|--|--|""",
"""  _______    
   |     |    
   |     O    
   |       
   |       
   |          
|--|--|""",
"""  _______    
   |     |    
   |     O    
   |     |   
   |       
   |          
|--|--|""",
"""  _______    
   |     |    
   |     O    
   |    /|  
   |       
   |          
|--|--|""",
"""  _______    
   |     |    
   |     O    
   |    /|\   
   |       
   |          
|--|--|""",
"""  _______    
   |     |    
   |     O    
   |    /|\   
   |    /    
   |          
|--|--|""",
"""  _______    
   |     |    
   |     O    
   |    /|\   
   |    / \   
   |          
|--|--|"""
           ]
while True:
   konec = 0
   pokus = 13
   odpoved = 0
   konec = "znova"
   pokusi = 0
   if konec == "konec":
        break
   elif konec == "znova":
      a = (random.choice(slova))
      vypocet = len(a)
      podtrzitka2 = podtrzitka[vypocet - 1]
      print(podtrzitka2)
      while True:
            pismeno = (input("hádej písmeno které si myslíš ,že je ve slově:"))
            if pismeno in a:
               print("tvoje písmeno je ve slově")
               p = a.index(pismeno)
               z = p + 1
               napoveda = podtrzitka2[:p] + pismeno + podtrzitka2[z:]
               podtrzitka2 = napoveda
               print(napoveda)
               if a == napoveda:
                   print("VYHRAL JSI")

            else:
               print("tvé písmeno není ve slově")
               print(sibenice[pokusi])
               pokusi = pokusi + 1
               pokus = pokus - 1
               print("máš ještě", pokus, "pokusu")
               if pokusi == 13:
                  print("prohrál jsi!")
                  break
   print("chceš-li hrát znova napiš: znova, chceš-li hru ukončit napiš: konec")
   konec = (input("znovu/konec:"))

