from funciones import *


def main4():
    '''Solicita un valor N y luego invoca a
       funcion4(N) para imprimir el resultado.'''
    try:
        nro = int(input('Ingrese un valor: '))
        print('Lista de numeros: ', function4(nro))
    except Exception as e:
        print('Ha ocurrido un error al generar la lista \n ' + str(e))
        raise


def main5():
    ''' Solicita un valor X y devuelve una cadena con el 
        mes al cual corresponde. '''
    try:
        nro = int(input('Ingrese un numero: '))
        print('El numero corresponde al mes: ' + function5(nro))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
        raise


def main6():
    ''' Solicita un valor X y genera una tabla
        con los multiplos hasta 10. '''
    try:
        numero = int(input("Ingrese un numero: "))
        print(function6(numero))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
        raise


def main7():
    ''' Solicita un entero e invoca a la function7
        para mostrar el resultado '''
    try:
        valor = int(input('Ingrese un valor: '))
        print(function7(valor, asc=False))
    except Exception as e:
        print('Ha ocurrido un error: ' + str(e))
        raise


def main8():
    ''' Solicita un caracter y una cadena e invoca
        a function8 para mostrar el resultado '''
    try:
        cadena = input('Ingrese una cadena: ')
        caracter = input('Ingrese un caracter: ')
        print(function8(cadena, caracter))
    except Exception as e:
        print('Ha ocurrido un error' + str(e))
        raise


def main9():
    try:
        ''' Se solicita una cadena y se llama a
            function9 para mostrar el resultado  '''
        cadena = input("Ingrese una cadena: ")
        print(function9(cadena))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
        raise


def main10():
    try:
        numeros = (5, 4, 3, 2, 1, 6, 45, 3, 6, 6, 6, 6, 6)
        numero = int(input("Ingrese un numero: "))
        print(function10(numeros, numero))
    except Exception as e:
        print(e)
        raise


def main11():
    numeros = (5, 4, 3, -2, 1, 6, 455, 3, 6, 6, 6, 6, 6)
    try:
        resultado = function11()
        print('El maximo es ', resultado[0])
        print('El minimo es ', resultado[1])
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
        raise


def main12():
    ''' Solicita una cadena y llama a function12() para mostrar 
        el resultado '''
    try:
        cadena = input('Ingrese una cadena: ')
        print('Es palíndromo: ' + str(function12(cadena)))
    except Exception as e:
        print('Ha ocurrido un error' + str(e))
        raise


def main13():
    try:
        ''' Se define una lista y se invoca a funcion13 para 
            mostrar los resultados '''
        regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
                   'patín', 'balón', 'reloj', 'bicicleta', 'anillo']
        print(function13(regalos))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))
        raise
