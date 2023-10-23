user = "Tomek"  # str
wiek = 39  # int - całkowite
wersja = 3.90001  # float zmiennoprzecinkowe
liczba = 134567112456  # int

print("witaj %s masz teraz %d lat" % (user, wiek))  # witaj Tomek masz teraz 39 lat
# print("witaj %s masz teraz %d lat" % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit
print("witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})
# witaj Tomek, masz teraz 39 lat.

print("witaj {} masz teraz {} lat".format(user, wiek))
print("witaj {} masz teraz {} lat".format(wiek, user))
# nie weryfikuje typów
print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - f-string - sformatowany string

print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.8)
print("Używamy wersji Python %.1f" % 3.8)
print("Używamy wersji Python %.2f" % 3.8)  # Używamy wersji Python 3.80
print("Używamy wersji Python %.0f" % 3.8)  # Używamy wersji Python 4
print("Używamy wersji Python %.f" % 3.8)  # Używamy wersji Python 4
# Uwaga - występuje zaokrąglenie przy wypisywaniu
print("Używamy wersji Python {}".format(wersja))  # Używamy wersji Python 3.90001
print(f"Używamy wersji Python {wersja}")
print(f"Używamy wersji Python {wersja:.1f}")
print(f"Używamy wersji Python {wersja:.2f}")
print(f"Używamy wersji Python {wersja:.0f}")

print(f"{user:>10}")  # "     Tomek"
print(f"{user:>20}")  # "               Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^10}")  # "  Tomek   "

print(liczba)
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,112,456
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.112.456
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 112 456
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
