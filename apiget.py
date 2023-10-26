# CRUD - create, read, update, delete
# HTTP - post. get, put/patch, delete
# baza - insert, select, update, delete
# REST API
import requests as re

# lub pip install requests

# url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

# NBP wskazuje aby użyc metody HTTP GET
response = re.get(url)
print(response)
# status odpowiedzi
# <Response [200]> - ok
# 3.. - błedy przegladarki np.: przekierowanie
# 4.. - błąd danych np: 404 - brak zasoby, 400 Bad Request
# 5.. - błedy wewnętrzne serwera,  np problem z baza
# W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
# W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
# W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat
# 400 Bad Request - Przekroczony limit
table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '207/A/NBP/2023', 'effectiveDate': '2023-10-25', 'mid': 4.4758}]}
print(type(table))  # <class 'dict'>
print(table.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
print(table['table'])  # A
for k in table.keys():
    print(k, table[k])
# table A
# currency euro
# code EUR
# rates [{'no': '207/A/NBP/2023', 'effectiveDate': '2023-10-25', 'mid': 4.4758}]
print(table['rates'][0])
for k in table['rates'][0]:
    print(k, table['rates'][0][k])
# no 207/A/NBP/2023
# effectiveDate 2023-10-25
# mid 4.4758
url_zloto = 'http://api.nbp.pl/api/cenyzlota'
response = re.get(url_zloto)
print(response)
gold = response.json()
print(gold)  # [{'data': '2023-10-26', 'cena': 269.6}]
print(gold[0]['cena'])  # 269.6
gold_dict = gold[0]
for k in gold_dict:
    print(k, "=>", gold_dict[k])
# 269.6
# data => 2023-10-26
# cena => 269.6
