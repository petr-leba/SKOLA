a = input("Zadej čísla oddělený mezerou: ").split()

a = [int(n) for n in a]

b = sorted(a, reverse=True)

print("Největší čísla jsou:", b[:3])
