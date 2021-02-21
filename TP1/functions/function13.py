#!/usr/bin/python3
import random

def function13(regalos):
    ''' Recibe una lista y devuelve una lista con elementos
        seleccionados del argumento seleccionados al azar. '''
    try:
        if len(regalos) < 1:
            raise ValueError
    except Exception as e:
        print('Argumento no valido ' + str(len(regalos)) + str(e))
        raise 
    else:
        sorteo_lista = []
        for sorteo in range(5):
            regalo = regalos[random.randint(0, 9)]
            sorteo_lista.append(regalo)

        return sorteo_lista

def main():
    try:
        ''' Se define una lista y se invoca a funcion13 para 
            mostrar los resultados '''
        regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
                   'patín', 'balón', 'reloj', 'bicicleta', 'anillo']
        print(function13(regalos))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))