#!/usr/bin/python3
import random

def function_4(n, asc=True):
    lista = []
    for i in range(n):
        num_aleatorio = random.randint(0, 9)
        lista.append(num_aleatorio)

    print(lista)
    lista.sort(reverse=asc)  # ordena la lista
    return lista

print(function_4(5, asc=False))
