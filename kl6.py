class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    """
    Menager
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 7500)
pracownik.przedstaw_sie()
pen_prac = pracownik.oblicz_pensje()
print(f"{pracownik.imie} Zarabiam {pen_prac} brutto")
menago = Manager("Anna", "Nowak", 15000, 5000)
menago.przedstaw_sie()
pen_menago = menago.oblicz_pensje()
print(f"{menago.imie} Zarabiam {pen_menago} brutto")
