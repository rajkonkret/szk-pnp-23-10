# krotka - jest niemutowalna(niezmienialna)
# zmienna - niezmienna

tupla = "Radek",
print(type(tupla))
temp = 36, 6
print(type(temp))  # <class 'tuple'>
tupla2 = "Tomek", "Asia", "Zbyszek", "Marek"
print(tupla2)  # ('Tomek', 'Asia', 'Zbyszek', 'Marek')
print(type(tupla2))  # <class 'tuple'>

tupla3 = (43, 55, 22.34, 11, 200)
print(tupla3)
print(type(tupla3))  # <class 'tuple'>

print(tupla2.index("Tomek"))  # 0
print(tupla2.count("Asia"))  # 1

a, b = 1, 2
print(a)
print(b)

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3]
# rozpakowanie tupli
imie, *imie2, imie3 = tupla2
print(imie)
print(imie2)
print(imie3)

*imie, imie2, imie3 = tupla2
print(imie)
print(imie2)
print(imie3)
print(sorted(tupla2))  # ['Asia', 'Marek', 'Tomek', 'Zbyszek']
print(tupla2)

lista = list(tupla2)
print(lista)
print(type(lista))  # <class 'list'>
