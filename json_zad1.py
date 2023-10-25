# json - {"name":"Radek"}
# obiekt typu klucz - wartosc
# odpowiednikiem jsona w pythonie jest słownik
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {"name": "Radek", "age": 40, "czy_pali": null}
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }
# posortowane
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as fh:
    data = json.load(fh)  # wczytanie jsona do słownika w pythonie

print(data)
print(type(data))  # <class 'dict'>
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(data['name'])  # Radek

json_text = json.dumps(data)
# zamiana słownika na json w formie str
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}
# zamiana jsona  na słownik
string_json = json.loads(json_text)
print(string_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
