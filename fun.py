# funkcja -  wydzielony fragment kodu, który można wykonac wielokrotnie

a = 6
b = 7


# deklarowanie funkcji, tylko zapamietuje to miejsce jako miejsce umieszczenia funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)  # wyświetli wynik działania


def dodaj2(a, b):  # funkcja z argumentami a i b (obowiązkowymi) zakres lokalny zmiennych a i b
    print(a + b)


# parametr opcjonalny pozwala zasymulowac przeciążanie funkcji liczbą argumentów
def odejmij(a, b, c=0):
    # a i b obowiązkowe, c ma wartośc domyślną
    print(a - b - c)


# uruchomienie funkcji: nazwa i nawiasy ()
dodaj()  # 13
dodaj2(5, 6)  # 11
odejmij(9, 5)  # 4
odejmij(9, 5, 2)  # 2
odejmij(b=5, a=9)  # przekazanie parametrów po nazwie
odejmij(c=2, b=5, a=9)
print(dodaj())  # None
# print(dodaj() + dodaj2(6, 7))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

