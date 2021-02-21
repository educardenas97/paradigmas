from funciones import *

def main4():
    '''Solicita un valor N y luego invoca a
       funcion4(N) para imprimir el resultado.'''
    try:
        nro = int(input('Ingrese un valor: '))
        print('Lista de numeros: ', function4(nro))
    except Exception as e:
        print('Ha ocurrido un error al generar la lista \n ' + str(e))


def main5():
    ''' Solicita un valor X y devuelve una cadena con el 
        mes al cual corresponde. '''
    try:
        nro = int(input('Ingrese un numero: '))
        print('El numero corresponde al mes: ' + function5(nro))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))


def main6():
    ''' Solicita un valor X y genera una tabla
        con los multiplos hasta 10. '''
    try:
        numero = int(input("Ingrese un numero: "))
        print(function6(numero))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))


def main7():
    ''' Solicita un entero e invoca a la function7
        para mostrar el resultado '''
    try:
        valor = int(input('Ingrese un valor: '))
        print(function7(valor, asc=False))
    except Exception as e:
        print('Ha ocurrido un error: ' + str(e))


def main8():
    ''' Solicita un caracter y una cadena e invoca
        a function8 para mostrar el resultado '''
    try:
        cadena = input('Ingrese una cadena: ')
        caracter = input('Ingrese un caracter: ')
        print(function8(cadena, caracter))
    except Exception as e:
        print('Ha ocurrido un error')


def main9():
    try:
        ''' Se solicita una cadena y se llama a
            function9 para mostrar el resultado  '''
        cadena = input("Ingrese una cadena: ")
        print(function9(cadena))
    except Exception as e:
        print('Ha ocurrido un error ')
