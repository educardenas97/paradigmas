#!/usr/bin/python3

def function6(numero):

    lista = []
    for i in range(1, 11):
        lista.append(i*numero)
    return lista


def main6():
    ''' Solicita un valor X y genera una tabla
        con los multiplos hasta 10. '''
    try:
        numero = int(input("Ingrese un numero: "))
        print(function6(numero))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
