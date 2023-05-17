list = []
biggestlist = []
zadavani = True

while(zadavani == True):
    x = input("Zadejte čísla ")
    if x == "konec":
        zadavani = False
        break
    else:
        x = int(x)
        list.append(x)

for i in range(3):
    biggest = max(list)
    biggestlist.append(biggest)
    print(biggest)
    list.remove(max(list))
    
print(biggestlist)