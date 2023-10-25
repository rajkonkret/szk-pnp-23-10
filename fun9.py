def odejmij(a, b):
    return a - b


print(odejmij(6, 7))
# lambda - skrócona forma funkcji
odejmij2 = lambda a, b: a - b  # return jest w labdzie domyslnie
print(odejmij2(6, 7))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(8))
print(wiek(15))
print(wiek(25))
# dziecko
# nastolatek
# dorosły

lista = [1, 2, 3, 4, 5, 6, 7, 8, 10, 23, 50]
l = []  # pusta lista

for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 10, 12, 14, 16, 20, 46, 100]


# map() - bierze kazdy elemnt z kolekcji, wykonuje na nim operacja wg zadanej funkcji

def zmien(x):
    return x * 2


print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 10, 12, 14, 16, 20, 46, 100]
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# lambda uzyta jako funkcja anonimowa zdefiniowana w miejscu wykonania
# filter() - bierze elementy kolekcji i sprawdza wg warunku zadanego funkcje
print(f'Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}')
# Zastosowanie filter(): [1, 2]
# wyflitrowac liste l warunkiem gdzie x > 8
# wyfiltrowac z lity l wieksze od 3, mniejsze od 20
print(f'Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}')
print(f'Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 20, l))}')
print(f'Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, l))}')
# x > 3 and x < 20  => 3 < x < 20
# Zastosowanie filter(): [4, 6, 8, 10, 12, 14, 16]
# # Zastosowanie filter(): [4, 6, 8, 10, 12, 14, 16]
