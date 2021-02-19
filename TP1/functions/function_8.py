#!/usr/bin/python3

cadena = input("Ingrese una cadena: ")


def function_8(cadena, caracter):
    lista = []
    for c in cadena:
        if c != caracter:
            lista.append(c)

    return "".join(map(str, lista))


print(function_8(cadena, "c"))
