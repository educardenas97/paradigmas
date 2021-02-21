#!/usr/bin/python3

def function12(cadena):
    ''' Recibe una cadena y determina si la misma es un palindromo '''
    try:
        if len(cadena) < 1:
            raise ValueError
    except Exception as e:
        print('Argumento invalido ')
        raise 
    else:
        cadena_al_reves = cadena[::-1]
        if cadena == cadena_al_reves:
            return True
        else:
            return False

def main():
    ''' Solicita una cadena y llama a function12() para mostrar 
        el resultado '''
    try:
        cadena = input('Ingrese una cadena: ')
        print('Es palíndromo: ' + str(function12(cadena)))
    except Exception as e:
        print('Ha ocurrido un error' + str(e))
        raise 