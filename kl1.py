# klasa - szablon
# klasa moze okreslac pola i funkcje
# instancją klasy jest obiekt
# obiekt - element zbudowany wg wytycznych zawartych w klasie


class Human:
    """
    Klasa opisująca Człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print(f"Wiek: {self.wiek}")


# wyswietlenie dokumentacjo dotyczacej klasy/funkcji
print(Human.__doc__)  # Klasa opisująca Człowieka w Pythonie
print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x0000022849105550>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
cz1.imie = "Ania"
cz1.wiek = "45"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
cz1.powitanie()

cz2 = Human()
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
cz2.imie = "Radek"
cz2.wiek = "45"
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
cz2.nazwisko = 'Kowalski'
print(cz2.nazwisko)
cz2.powitanie()  # Nazywam się Radek
cz1.podaj_wiek()
cz2.podaj_wiek()
