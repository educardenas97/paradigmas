#!/usr/bin/python3

def function_3(numero):
    lista = []
    for i in range(1, 11):
        lista.append(i*numero)
    return lista


numero = int(input("Ingrese un numero: "))
print(function_3(numero))
