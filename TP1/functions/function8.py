#!/usr/bin/python3

def function8(cadena, caracter):
    ''' Recibe un cadena y un caracter, y retorna una cadena 
        sin el caracter ingresado. '''
    try:
        if len(cadena) < 1 or len(caracter) < 1:
            raise Exception('Argumento no valido')
    except Exception as e:
        valor = caracter if cadena > 0 else cadena
        print('Ingrese una cadena/caracter' + str(valor))
    else:
        lista = []
        for c in cadena:
            if c != caracter:
                lista.append(c)

        return "".join(map(str, lista))


def main():
    ''' Solicita un caracter y una cadena e invoca
        a function8 para mostrar el resultado '''
    try:
        cadena = input('Ingrese una cadena: ')
        caracter = input('Ingrese un caracter: ')
        print(function8(cadena, caracter))
    except Exception as e:
        print('Ha ocurrido un error')
