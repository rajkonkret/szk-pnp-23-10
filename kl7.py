# klaass abstrakcyjna - klasa dla której nie mozna stworzyc obiektów
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pyhonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstarakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Kokokokoko")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("kiiiiir ki-er")

# Po dodaniu @abstractmethod klasa stałą sie abstrakcyjna
# nie można utworzyc obiektu takiej klasy
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# orzel = Ptak("Orzel", 48)
# orzel.latam()
#
# kur = Ptak("Kura", 0)
# kur.latam()
kur2 = Kura("Kura")
kur2.latam()
kur2.wydaj_odglos()

or2 = Orzel("Orzel", 48)
or2.latam()
or2.wydaj_odglos()
