a = []
while True:
    
    a.append(int(input("zadej cislo")))
    b = len(a)
    print(b)
    if b == 10:
        print("mas jich 10")
        break
for i in range(3):
    c = max(a)
    print(c)
    a.remove(c)
        