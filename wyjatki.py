# napisac program kalkulator z wykorzystaniem pętli while True
# menu z dostepnymi działaniami
# pobrac wybrana opcje
# pobrac o uzytkownika liczby do oblicznen
# wyswietlic wynik obliczenia

while True:
    print("""
        1. Dodawanie
        2. Odejmowanie
        3. Mnożenie
        4. Dzielenie
        5. Koniec
        """)
    odp = input("Podaj opcje z menu")
    if odp >= "5":
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))
        if odp == '1':
            print(a + b)
        elif odp == '2':
            print(a - b)
        elif odp == '3':
            print(a * b)
        elif odp == '4':
            # if b != 0:
            print(a / b)
            # else:
            # print("Nie dziel przez zero")
        else:
            print("nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Błąd wartości")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Wystąpił błąd", e)
    else:
        print("Tylko gdy nie ma błedu")
    finally:
        print("Wykonuje się zawsze")
