# if - warunek - instrukcja sterowania przepływem

odp = True  # True - prawda, False - fałsz
if odp:
    print("Brawo")
else:  # w przeciwnym przypadku
    print('Ucz się dalej')

print("Idę dalej")

# podatek = 0.9
# zarobki = int(input('Podaj dochód'))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Płacisz {zarobki * podatek}")
# kolejnosc ma znaczenie

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabacik wynosi: {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi: {rabat}")
# Rabacik wynosi: 25
# Rabat wynosi: 25

# zasymulejemy system zbieranie logów i wyswietlanie komunikatów
# w zależnosci od tego jaki system i jaki komunikat przysłał.
lista_bledow = []
alert_system = "console"
error = "critical"
error_message = "Stało się coś strasznego"

if alert_system == 'email':
    print(error_message)
elif alert_system == 'console':
    if error == "medium":
        lista_bledow.append("ostrzezenie")
    elif error == "critical":
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny")

print(lista_bledow)
# dodac gdy z consoli przyjdzie błąd critical wpis krytyczny do listy
# zrobic test z historii, geografi, czegokolwiek
# zadac pytanie
# odczytac odpowiedz
# sprawdzic odpowiedz i ocenic
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print("Brawo")
else:
    print("Masz wksiązce na strinie 23")
# 13:35
