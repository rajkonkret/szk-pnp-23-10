# set - zbiór - prxzechowuje niezduplikowane elementy
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # pusty zbiór
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}
zbior.pop()
zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}

zbior.remove(55)
zbior.remove(18)
print(zbior)

lista = list(zbior)
print(lista)  # [44, 22]

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}
print(zbior | zbior2)  # suma zbiorów  {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior & zbior2)  # cześć wspólna  {44}
print(zbior - zbior2)  # różnica {22}
print(zbior.difference(zbior2))  # {22}
