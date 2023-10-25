# / oddziela argumenty, ktore muszą byc podane po pozycji od argumentów, które mogą byc podane po nazwie
def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)
allparams(1, 2, 3)  # c, d 3 256
allparams(1, 2, 3, 4)  # args (4,)
allparams(1, 2, 3, 4, 5)  # args (4, 5)
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11)  # args (4, 5, 6, 7, 8, 9, 0, 10, 11)
allparams(1, 2, 3, 4, 5, 6, d=100)  # c, d 3 100
allparams(1, 2, 3, 4, 5, 6, d=100, e=5456, name='Radek')  # kwargs {'e': 5456, 'name': 'Radek'}
# allparams(a=1, b=2)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# jesli mamy / w argumentach
# a i b musimy przekazac obowiazkowo jako arg pozycyjne
allparams(1, 2)  # a, b 1 2
allparams(1, 2, c=9)  # c, d 9 256
allparams(1, 2, a=5, b=9)
# a, b 1 2
# c, d 42 256
# args ()
# kwargs {'a': 5, 'b': 9}
