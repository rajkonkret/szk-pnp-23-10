import csv

lista = []

with open('dane_2.csv', 'r') as file:
    reader = csv.reader(file)
    for i in reader:
        lista.append(i)

print(lista)
# [['SN', ' Name', ' City'], ['1', ' Michael', ' New Jersey'], ['2', ' Jack', ' California']]
print(lista[1][1])  # " Michael"

lista[1][1] = "Radek"
with open('dane_nowe.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(lista)