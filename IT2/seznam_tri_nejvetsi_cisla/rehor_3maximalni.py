cisla = input("Zadejte seznam cisel (oddelenych carkou): ")
cisla_list = [int(x) for x in cisla.split(",")]

cisla_list.sort(reverse=True)
nejvetsi_cisla = cisla_list[:3]

print("Tri nejvetsi cisla v seznamu jsou:", nejvetsi_cisla)
