cisla = input("Zadej seznam cisel oddelenych mezerou: ")
cisla_list = cisla.split()
cisla_list = [int(cislo) for cislo in cisla_list]

cisla_list.sort(reverse=True)
print("Tři největší čísla v seznamu jsou:", cisla_list[0], cisla_list[1], cisla_list[2])