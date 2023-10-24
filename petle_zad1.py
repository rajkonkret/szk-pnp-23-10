# for - petla iteracyjna
import random

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ - niema zmienna
    # print(_)
    pass

for i in range(10):
    print(i * 2)

lista2 = list(range(1, 50))  # int od 1..49 - generowanie listy liczb od 1 do 49
lista_wynik = []
for i in range(6):  # 0..5 bedzie 6 liczb
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    lista_wynik.append(wyn)
print(lista_wynik)
lista_wynik.sort()
print(lista_wynik)

for i in range(10):
    if i % 2 == 0:  # modulo - reszta z dzielenia
        print(i, "jest parzysta")
# zapis jednolinijkowy petli for z dodaniem do listy
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)

print(lista3)  # [0, 2, 4, 6, 8]
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)  # 3

a = 1
a += 1  # a = a +1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0
# dzielenie daje wynik typu float()
a %= 2  # a = a % 2 modulo(reszta z dzielenia)
print(a)  # 1.0

imiona = ["Radek", "Zenek", 'Monika']
print(imiona)
print(type(imiona))

for p in imiona:
    print(p)

# wyswietlic elemnty z listy ale z indeksem
# 0 Radek
for p in imiona:
    print(imiona.index(p), p)  # 0 Radek

for i in range(len(imiona)):  # range(3) => 0, 1, 2
    print(i, imiona[i])

# enumerate() - numeruje kolekcje
for p in enumerate(imiona):
    print(p)  # (2, 'Monika')
for p, o in enumerate(imiona):
    print(p, o)

ludzie = ['Radek', 'Janek', 'Asia', 'Michał', "Tadek"]
wiek = [47, 67, 32, 34]

# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])  # gdy rózne długości list => IndexError: list index out of range
# zip() - łączy kolekcje
for i in zip(ludzie, wiek):
    print(i)  # ('Radek', 47)

# ('Radek', 47)
# ('Janek', 67)
# ('Asia', 32)
# ('Michał', 34)
for l, w in zip(ludzie, wiek):
    print(l, w, sep=";", end="")  # Radek;47Janek;67Asia;32Michał;34
print()

"""
    Prints the values to a stream, or to sys.stdout by default.

      sep
        string inserted between values, default a space.
      end
        string appended after the last value, default a newline.
      file
        a file-like object (stream); defaults to the current sys.stdout.
      flush
        whether to forcibly flush the stream.
    """
for i in range(0, 10, 2):  # 0..9 co drugą start, stop, krok
    print(i)

for i in range(0, -10, -2):  # krok ujemny, pętla do tyłu
    print(i)
# wypisac 0 Radek 47
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (3, ('Michał', 34))
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Radek 47
# 1 Janek 67
# 2 Asia 32
# 3 Michał 34
# i, (l, w)  - i z krotki zewnetrznej, (l,w) - elemnty wewnetrznej krotki, muszą byc w nawiasie
# (3, ('Michał', 34))
for i, w in enumerate(zip(ludzie, wiek)):
    print(i, w)  # 0 ('Radek', 47)
ind, we = (0, ('Radek', 47))
print(ind)  # 0
print(we)  # ('Radek', 47)
l, w = ('Radek', 47)  # rozpakowanie drugiej krotki
print(l)
print(w)
