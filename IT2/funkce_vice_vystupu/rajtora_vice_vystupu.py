a = 10
b = 30
c = 20


def bigg_numb(*seznam):
    cisla_list = list(seznam)
    cisla_list.sort()
    print(cisla_list)
    return cisla_list



a, b, c = bigg_numb(a, b, c,)


