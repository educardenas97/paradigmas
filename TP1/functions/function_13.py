#!/usr/bin/python3
import random

regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']

def function_13(regalos):
    sorteo_lista = []
    for sorteo in range(5):
        regalo = regalos[random.randint(0, 9)]
        sorteo_lista.append(regalo)

    return sorteo_lista

print(function_13(regalos))
