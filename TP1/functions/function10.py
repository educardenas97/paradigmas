#!/usr/bin/python3

def function10(numeros, numero):
    ''' Recibe una lista con numeros y un numero
        devuelve las apariciones de dicho numero en la lista proporcionada. '''
    try:
        if len(numeros) < 1 or numero == None:
            raise ValueError
    except Exception as e:
        raise Exception('Argumento no valido ')
    else:
        contador = 0
        for i in numeros:
            if numero == i:
                contador = contador+1
        return contador

def main10():
    try:
        numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)
        numero = int(input("Ingrese un numero: "))
        print(function10(numeros, numero))
    except Exception as e:
        print(e)
        raise 