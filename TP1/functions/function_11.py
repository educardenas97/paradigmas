#!/usr/bin/python3

numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)

def funcion_11(numeros):
    maximo = numeros[0]
    minimo = numeros[0]

    for i in numeros:
        if i > maximo:
            maximo = i

        if i < minimo:
            minimo = i
    
    return (minimo,maximo)

print("El maximo es ", funcion_11(numeros)[0])
print("El minimo es ", funcion_11(numeros)[1])
