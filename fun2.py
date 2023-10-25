# funkcje zwracające wynik
# muszą byc zakończone słowem return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 9))
# napisac funkcję zwracjącą wynik, mającą trzy parametry z wartosciami domyślnymi
# wypisac mozliwe sposoby jej wywołania
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij())
print(odejmij(c=9, b=9))
print(odejmij(c=9, a=9, b=7))
print(odejmij(1, c=9, b=8))
# print(odejmij(b=8,c=9,2))  # SyntaxError: positional argument follows keyword argument

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(vat=15, cena=1000))
# 1230.0
# 1070.0
# 1150.0
# 11:15
