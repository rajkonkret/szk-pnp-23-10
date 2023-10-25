a = 10
b = 10


def dodaj():
    a = 6  # a i b zadeklarowane lokalnie
    b = 7  # nie wpływaja na wartosc globalna
    print(a + b)


def dodaj2():  # uzyje a z globalnego scopa(zakresu)
    print(a + b)


def dodaj3():
    global a
    a = 6
    b = 7
    print(a + b)


def dodaj4(a, b):
    print(a, b)


print(f"Zmiennna a z góry {a}")  # Zmiennna a z góry 10
dodaj()  # 13
print(f"Zmiennna a z góry {a}")  # Zmiennna a z góry 10
dodaj2()  # 20
print(f"Zmiennna a z góry {a}")  # Zmiennna a z góry 10
dodaj3()
print(f"Zmiennna a z góry {a}")  # Zmiennna a z góry 6
dodaj2()  # 16
dodaj4(a, b)
