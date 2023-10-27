import pickle  # wspomaga działanie ze złożonymi danymi

lista = [1, 2, 3, 4, 5]
with open('test_lista.txt', 'w') as f:
    f.write(str(lista))

with open('test_lista.txt', 'r') as f:
    lines = f.read()

print(lines)  # [1, 2, 3, 4, 5]
print(type(lines))  # <class 'str'>
print(list(lines))  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']

# wb - zapis bajtowy - tak wymaga pickle
with open('lista_pickle.log', 'wb') as file:
    pickle.dump(lista, file)

# rb - odczyt bajtowy
with open('lista_pickle.log', "rb") as file:
    loaded_list = pickle.load(file)

print(loaded_list)
print(type(loaded_list))
print(loaded_list[0])

# [1, 2, 3, 4, 5]
# <class 'str'>
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']
# [1, 2, 3, 4, 5]
# <class 'list'>
1
