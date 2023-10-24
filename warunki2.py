# match case - instrukcja sterowania przepływem
lista = []
lang = input("Podaj znany ci język programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:  # domyslny - odpowiednik else
        print('nie znam takiego języka')
print(lista)