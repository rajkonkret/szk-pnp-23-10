# dziedziczenie
class Pojazd:
    """
    klasa opisująca pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):
    """
    Klasa opsiujaca samochod
    """

    def __init__(self, kolor, marka):  # inicjalizator dla klasy samochod
        # pass
        super().__init__(kolor)  # wywołanie inicjalizatora z klasy wyzszej
        self.marka = marka

    def info(self):
        """
        metoda informujaca o cechach obiektu
        :return: None
        """
        # print(f"{self.marka} : {self.kolor}")
        super().info()  # można uzyc metody z klasy wyzszej
        print(f"Samochód: {self.marka}")


poj = Pojazd("zielony")
poj.info()

sam = Samochod("czerwony", "Maserati")
sam.info()

print(sam.__doc__)  # wypisanie dokumentacji klasy
print(sam.info.__doc__)  # wypisanie dokumentacji metody w klasie
