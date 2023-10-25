def liczby(name="Nie ma ucznia", *cyfry):
    print(cyfry)
    print(type(cyfry))
    suma = 0
    try:
        for c in cyfry:
            suma += c
        print(suma)
        count = len(cyfry)
        print(count)
        print(f"Średnia dla ucznia {name} wynosi {suma / count}")
    except ZeroDivisionError:
        print(f"Uczeń {name} nie ma ocen!!!")
    except Exception as e:
        print("Błąd", e)


liczby("Adam", 1, 2, 3)
liczby("Radek")
liczby("Zenek", 1, 2, 3, 4, 5, 6)
liczby()
