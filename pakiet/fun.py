def powitanie():
    print("Cześć")


def info():
    print("Jestem pakietem")


print(__name__)
# gdy program uruchamiany bezposrednio
# __name__ ma  wartosc __main__
# gdy program jest uruchamiany z pakietu
# __name__ ma wartosc nazwy pakietu jaki wywołał np.: pakiet.fun
if __name__ == '__main__':
    print("Coś dowolnego")
