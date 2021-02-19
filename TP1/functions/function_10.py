#!/usr/bin/python3

numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)

numero = int(input("Ingrese un numero: "))

def function_10(numeros, numero):
    contador = 0
    for i in numeros:
        if numero == i:
            contador = contador+1
    return contador

print(function_10(numeros, numero))