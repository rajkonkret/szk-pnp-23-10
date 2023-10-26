# pliki csv - dane rozdzielone przecinkiem lub innym dopuszczonym znakiem podziału

# Zenek, Michał, Radek, Monika
import csv

# biblioteka do pracy z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

filename = 'records.csv'
dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'},
    {'name': 'Zosia', 'branch': 'cos', 'year': '2', 'cgpa': '9'},
    {'name': 'Asia', 'branch': 'cot', 'year': '4', 'cgpa': '9.1'},
    {'name': 'Monika', 'branch': 'cob', 'year': '5', 'cgpa': '11'},
    {'name': 'Zenek', 'branch': 'coo', 'year': '7', 'cgpa': '11.5'},
]
dict_2 = dict(zip(fields, row))
print(dict_2)

with open(filename, 'w', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=",")
    # csvwriter.writerow(row)  - zapisanie pojedynczego wiersza z listy
    csvwriter.writeheader()  # zapisanie nagłowka czyli nazw kolumn
    csvwriter.writerow(dict_2)  # zapisanie danych ze słownika do csv
    csvwriter.writerows(dict_list)  # zapisanie listy słowników jako kolejnych wierszy
