# słownik - para klucz wartość
# {"name" : "Radek"}
# klucze nie mogą się powtarzać

dictionary = {}  # pusty słownik
print(type(dictionary))  # <class 'dict'>

dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
# dict_values(['Radek', 39])
# dict_keys(['imie', 'wiek'])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dictionary.update({"date": '12-12-2023'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dict2 = {'x': 2}
dict2.update([("y", 5), ("z", 7)])
print(dict2)  # {'x': 2, 'y': 5, 'z': 7}

# utworzyc słownik gdzie będą pary polskie słowo - angielskie tłuamczenie
dict_p_e = {"imie": "name", "kot": "cat"}
dict_test = {}
dict_test["kot"] = "cat"
dict_test.update({"imie": "name"})
print(dict_p_e['imie'])  # name
print(f"Umiem przetłuamczyć {dict_p_e.keys()}")
key = input("Podaj słowo do przetłuamczenia")  # pobieranie danych od użytkownika, zawsze zwraca str
print(dict_p_e[key.lower().replace(" ", "")])
# lower() - zamiana na małe, replace() - zamiana spacji na pusty ciąg znaków

# kalkulator
# pobrac a i b od uzytkownika
# wyswietlic wynik dodawania
a = int(input("Podaj pierwszą liczbę"))
b = input("Podaj drugą liczbę")
print(a + int(b))
# int() rzutowanie na int(całkowite) float() - rzutowanie na zmiennoprzecinkowe
# 11:15
