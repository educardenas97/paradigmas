#!/usr/bin/python3

def function4(n):
    '''Retorna una lista con enteros generados de 1 a N'''
    try:
        if n <= 0:
            raise Exception('Argumento invalido. ')
    except Exception as e:
        print('No es posible generar la lista para ' + str(n))
        raise 
    else:
        lista = []
        i = 1
        while i <= n:
            lista.append(i)
            i = i + 1

        return lista


def main4():
    '''Solicita un valor N y luego invoca a
       funcion4(N) para imprimir el resultado.'''
    try:
        nro = int(input('Ingrese un valor: '))
        print('Lista de numeros: ', function4(nro))
    except Exception as e:
        print('Ha ocurrido un error al generar la lista \n ' + str(e))