#!/usr/bin/python3
import random

def function7(n, asc=True):
    ''' Recibe un numero n y retorna una lista ordenada generada
        de manera aleatoria. '''
    lista = []
    for i in range(n):
        num_aleatorio = random.randint(0, 9)
        lista.append(num_aleatorio)

    lista.sort(reverse=asc)  # ordena la lista
    return lista


def main7():
    try:
        valor = int(input('Ingrese un valor: '))
        print(function7(valor, asc=False))
    except Exception as e:
        print('Ha ocurrido un error: ' + str(e))

