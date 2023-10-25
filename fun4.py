# funkcje zagnieżdzone
def fun1():
    print("To jest fun1")

    def fun2():  # Funkcja zagnieżdzona (definicja)
        print("To jest fun2")

    return fun2  # zwracamy tylko adres funkcji(nie dajemy ())


print(fun1())  # <function fun1.<locals>.fun2 at 0x0000021B5AE2CC20>
xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x000001E1868DCC20>
print(type(xfun))  # <class 'function'>
xfun()
