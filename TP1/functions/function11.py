#!/usr/bin/python3

def function11(numeros):
    ''' Recibe una tupla con numeros y devuelve una tupla con el mayor
        y menor de los elementos.  '''
    try:
        if numeros == None:
            raise ValueError
    except Exception as e:
        print('Argumento no valido ' + str(numeros))
        raise 
    else:
        maximo = numeros[0]
        minimo = numeros[0]
        for i in numeros:
            if i > maximo:
                maximo = i
            if i < minimo:
                minimo = i
        return (minimo,maximo)


def main():
    numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)
    try:
        resultado = function11()
        print('El maximo es ', resultado[0])
        print('El minimo es ', resultado[1])
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
        raise 