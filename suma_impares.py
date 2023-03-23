from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado= filter(lambda x: x % 2, lista)
suma_de_elemtos= reduce(lambda a, b: a+b, filtrado)
print(suma_de_elemtos)