#!/usr/bin/python3

cadena = input("Ingrese una cadena: ")
print(cadena)


def function_9(cadena):
    lista = []
    for c in cadena:
        if c not in lista:
            lista.append(c)
            
    return "".join(map(str, lista))


print(function_9(cadena))
