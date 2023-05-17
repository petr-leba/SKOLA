print("řádek")

for i in range(1):
    for i in range(5):
        print("*", end="")
    print()

print("čtverec")

for i in range(5):
    for i in range(5):
        print(" * ", end="")
    print()

print("obdélník")

for i in range(5):
    for i in range(10):
        print("* ", end="")
    print()

print("trojúhelník")

a=1
for i in range(10):
    for i in range(a):
        print("*", end="")
    print()
    a=a+1