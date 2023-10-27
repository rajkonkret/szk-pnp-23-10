# dekorator
# dodaje do funkcji dotakowe własciwosci

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # tu z () bo wynik działania

    return wew  # tu bez nawiasów bo adres w pamieci(referencję)


@dekor  # udekorowanie funkcji funkcją dekor
def hej():
    print("Hej!!!")


hej()
# dk = dekor(hej)
# dk()
# Hej!!!
# Dekorujemy
# Hej!!!

# po dodaniu @dekor do funkcji hej
# Dekorujemy
# Hej!!!
