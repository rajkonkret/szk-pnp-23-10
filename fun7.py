def connect(**opcje):  # parametry słownikowe
    print("funkcja connect")
    print("opcje", opcje)
    print(type(opcje))  # <class 'dict'>

    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    connect_param['pwd'] = opcje
    print("słownik w słowniku", connect_param)


def connect_all(*args, **kwargs):
    print("funkcja connect_all")
    print("args", args)  # pozycyjne bo *
    print("kwargs", kwargs)  # nazwane bo **


connect(a=6, b=8, c=9)  # parametry nazwane
# {'a': 6, 'b': 8, 'c': 9}
# przy takiej konstrukcji funkcji wszystkie parametry
# przekazywane do funkcji po nazwie zostaną zamienione
# pary klucz:wartość w słowniku
connect()
connect(name='Radek')

connect_all(1, 2)
connect_all(1, 2, a=8)
# (1, 2)  - args
# {'a': 8} - kwargs
connect(a=9)
# (1, 2)
# {}
# (1, 2)
# {'a': 8}
# {'a': 9}
# <class 'dict'>
# {'host': '127.0.0.7', 'port': '8080'}
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 9}}
# 13:30
# C:\Users\cscomarch\PycharmProjects\szk-pnp-23-10\venv\Scripts\python.exe C:\Users\cscomarch\PycharmProjects\szk-pnp-23-10\fun7.py
# funkcja connect
# opcje {'a': 6, 'b': 8, 'c': 9}
# <class 'dict'>
# {'host': '127.0.0.7', 'port': '8080'}
# słownik w słowniku {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 6, 'b': 8, 'c': 9}}
# funkcja connect
# opcje {}
# <class 'dict'>
# {'host': '127.0.0.7', 'port': '8080'}
# słownik w słowniku {'host': '127.0.0.7', 'port': '8080', 'pwd': {}}
# funkcja connect
# opcje {'name': 'Radek'}
# <class 'dict'>
# {'host': '127.0.0.7', 'port': '8080'}
# słownik w słowniku {'host': '127.0.0.7', 'port': '8080', 'pwd': {'name': 'Radek'}}
# funkcja connect_all
# args (1, 2)
# kwargs {}
# funkcja connect_all
# args (1, 2)
# kwargs {'a': 8}
# funkcja connect
# opcje {'a': 9}
# <class 'dict'>
# {'host': '127.0.0.7', 'port': '8080'}
# słownik w słowniku {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 9}}
#
# Process finished with exit code 0
# 13:40
