import pandas as pd

# excel_data = pd.read_excel('sales.xlsx', sheet_name="Arkusz1")
excel_data = pd.read_excel('sales.xlsx')
print(excel_data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000
data = pd.DataFrame(excel_data)
print("The content is: \n", data)  # \n - nowa linia
# The content is:
#    Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

print(data.values)
print(data.columns)
print(data.items)
print(data.index[-1])
# 3
print(data.index.max())  # ostatni numer indexu wiersza
# (ostatni numer wiersza)
# 3
print(data.tail(1))  # ostatni wiersz , tail( zwraca ostatnie n wierszy, gdy n=1 zwraca ostatni wiersz
# dtype: object
#   Sales Date    Sales Person  Amount
# 3 2021-04-07  Mahmudul Hasan   30000

print(data.columns[0])
print(type(data.columns[0]))  # <class 'str'>
print()
print(data.columns[2])  # Amount
print(data.iloc[1, 2])  # konkretna komórka
print("----------")
print("Wiersz", data.iloc[1])  # wiersz

print("-----------")
print("Wiersz", type(data.iloc[1]))  # wiersz
print("----------")
print("Wiersz2:", data.loc[1])
print("-------------")
for i in data.iloc[1]:
    print(i)

print(data.loc[1, "Amount"])  # mozna podac po nazwie kolumny
print(data.iloc[1, 2])  # trzeb apodac indeks kolumny
for i, e in enumerate(data.iloc[1]):  # wypisanie wartosci z wiersza o indeksie 1 i wskazanie przypisania do kolumn
    print(data.columns[i], ":", e)
# 13:40
