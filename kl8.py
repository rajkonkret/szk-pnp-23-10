# wielodziedziczenie
# W Pythonie klasa moze dziedziczyc po wielu klasa

class A:
    def method(self):
        print('Metoda z kalsy A')


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):
    """
    klasa C dziedziczy po klasie A i po klasie B
    """

    def method(self):
        print("Metoda z kalsy C")
        super().method()
        B.method(self)


# storzyc obiekt klasy A i B, uzyc na nich method()
a = A()
a.method()
b = B()
b.method()
c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# kolejnosc w zapisie dziedziczenia ma znaczenie C(B,A)
# C(A,B)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# Metoda z kalsy A
# Metoda z klasy B
# Metoda z kalsy A
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# po nadpianiu method() w klasie C mamy wynik:
# Metoda z klasy C
# po dodaniu w method() w klasie C super().method() czyli wywołania metody z kalsy wyzszej mamy wynik:
# Metoda z kalsy C
# Metoda z kalsy A - pierwsza w kolejnosci wg __mro__
# mozemy wskazac z której klasy ma byc uzyta method()
# B.method(self)
# wynik: (dla klasy C)
# Metoda z kalsy C
# Metoda z kalsy A
# Metoda z klasy B
