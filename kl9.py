class MyException(Exception):  # dziedziczymy po klaiw Exception - głównym wyjątku w Pythonie
    def __init__(self, message):
        super().__init__(message)


try:
    # print(6 / 0)
    raise ValueError("Bład wartosci")  # Błąd Bład wartosci
    # po wystapieniu pierwszego błedu program przerywa działanie i kieruje sie do sekcji obsługi błedów
    raise MyException("Wystąpił wyjątek")  # raise Rzucenie wyjątku
except ZeroDivisionError:
    print("Dzielenie przez zero")
except MyException:
    print("Wystąpił wyjatek MyException")
except Exception as e:  # worek na pozostałe błedy
    print('Błąd:', e)

print('Program nadal działa')
