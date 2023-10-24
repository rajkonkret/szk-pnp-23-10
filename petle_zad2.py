dictionary = {'imie': "Radek", 'nazwisko': "kowalski"}
print(dictionary)
print(type(dictionary))  # <class 'dict'>

# zwraca klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# zwraca wartości
for v in dictionary.values():
    print(v)

# zwraca pary
for p in dictionary.items():
    print(p)  # ('nazwisko', 'kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => kowalski

dict1 = {'name': 'imie', 'company': 'Comarch'}
print(dict1)  # {'name': 'imie', 'company': 'Comarch'}
print(type(dict1))  # <class 'dict'>
print({value: key for key, value in dict1.items()})
# { value: key}
# {'imie': 'name', 'Comarch': 'company'}
d2 = {}
for key, value in dict1.items():
    # d2.update({value: key})
    d2[value] = key
print(d2)
# <class 'dict'>
# {'imie': 'name', 'Comarch': 'company'}
# {'imie': 'name', 'Comarch': 'company'}
