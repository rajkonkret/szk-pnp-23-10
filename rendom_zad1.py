import random

# random - bibliotego do dziłanai z liczbami pseudolosowymi

print(random.randint(1, 6))  # 1..6 int
print(random.random())  # float 0...0.999999
print(random.random() * 6)  # float od 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))  # 56

lista2 = list(range(1, 50))  # int od 1..49 - generowanie listy liczb od 1 do 49
print(lista2)

lista_wynik = []
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)

print(lista_wynik)  # [3, 1, 25, 42, 18, 23]

print(random.choices(lista2, k=6))  # [9, 43, 17, 4, 4, 19]
print(random.sample(lista2, 6))  # [41, 0, 28, 47, 25, 3]
