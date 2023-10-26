class Human:
    """
    Klasa człowiek w Pythonie
    """

    def __init__(self, imie, wiek, plec="k"):  # inicjalizator, konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(f"Mam na imię {self.imie}")

    def podaj_wiek(self):
        print(f"Wiek: {self.wiek}")

    def podaj_plec(self):
        print(f"Plec: {self.plec}")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Ania", "39")
print(cz1.wiek)
print(cz1.plec)
print(cz1.imie)
cz1.powitanie()
# dopisac metody podaj_wiek, podaj_plec
cz1.podaj_wiek()
cz1.podaj_plec()
cz1.ruszaj()
cz2 = Human("Radek", 48, "m")
cz2.ruszaj()
