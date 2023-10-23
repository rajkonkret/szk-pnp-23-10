# clean code
# PEP8 - ctrl alt l - formatowanie kodu
print()  # wydrukuj/wypisz
print("Nazywam się Radek")  # w cudzysłowiu umieszcamy tekst (str)
print("Nazywam się Radek")  # w cudzysłowiu umieszcamy tekst (str)
print("Nazywam się Radek")  # w cudzysłowiu umieszcamy tekst (str)
print("Nazywam się Radek")  # w cudzysłowiu umieszcamy tekst (str)
print("Nazywam się Radek")  # w cudzysłowiu umieszcamy tekst (str)
print("Nazywam się Radek")  # w cudzysłowiu umieszcamy tekst (str)
print('Nazywam się Radek')  # w cudzysłowiu umieszcamy tekst (str)
# ctrl d - kopiowanie linii
print(type("Radek"))  # <class 'str'> teksty
# type() - zwraca typ jakiego rodzaju podaliśmy argument

print(39)
print(type(39))  # <class 'int'> liczby całkowite

print("39" + "15")  # łaczenie tekstów - konkatenacja
print(39 + 15)
print(5 * "4")

# zmienne - pudełko na dane
imie = "Radek"
print(type(imie))
print(imie)

imie = 47
print(type(imie))
print(imie)

wiek = 48
print(type(wiek))
print(wiek)
print(wiek + imie)

imie = "Radek"
# ctrl /  - komentarz lini pod kursorem
# print(wiek + imie)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print((str(wiek) + imie))  # str() - zamiana - rzutowanie na str. 48Radek

print(int("34") + int("54"))  # int() - rzutowanie na int, zamiana na int
