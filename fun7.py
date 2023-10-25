def connect(**opcje):  # parametry słownikowe
    print(opcje)
    print(type(opcje))  # <class 'dict'>

    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    connect_param['pwd'] = opcje
    print(connect_param)


def connect_all(*args, **kwargs):
    print(args)  # pozycyjne bo *
    print(kwargs)  # nazwane bo **


connect(a=6, b=8, c=9)  # parametry nazwane
# {'a': 6, 'b': 8, 'c': 9}
# przy takiej konstrukcji funkcji wszystkie parametry
# przekazywane do funkcji po nazwie zostaną zamienione
# pary klucz:wartość w słowniku
connect()
connect(name='Radek')

connect_all(1, 2)
connect_all(1, 2, a=8)
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
