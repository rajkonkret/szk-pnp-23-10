# stworzenia funkcji kantor zawierajacej dwie funkcje usd i eur
# wykorzystanie funkcji wewnętrznych w zależnosci od parametru inicjującego

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print(f"wymieniam {kwota} dol = {kwota * 4.10}")

    def eur(kwota=0):
        print(f"wymieniam {kwota} eur = {kwota * 4.50}")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
kantor_usd()  # dolary
# dodac mozliwosc przekazywania kwoty do wymiany
# ładnie wypisac przeliczoną kwotę
# np: wymieniam 100 dol = 410 pln
kantor_usd(1000)

# stworzyc i użyc kantor eur
kantor_eur = kantor('eur')
kantor_eur(1000)
