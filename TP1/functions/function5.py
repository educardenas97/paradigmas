#!/usr/bin/python3

def function5(numero):
    ''' Retorna un cadena con el mes correspondiente al numero dado. '''

    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    try:
        if numero in range(len(meses)):
            return meses[numero-1]
        else:
            raise Exception('Argumento invalido')
    except Exception as e:
        print('Valor fuera de rango: ' + str(numero))
        raise 

def main5():
    ''' Solicita un valor X y devuelve una cadena con el 
        mes al cual corresponde. '''
    try:
        nro = int(input('Ingrese un numero: '))
        print('El numero corresponde al mes: ' + function5(nro))
    except Exception as e:
        print('Ha ocurrido un error ' + str(e))

