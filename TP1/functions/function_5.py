#!/usr/bin/python3

def function_2(numero):
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    if numero in range(len(meses)):
        return meses[numero-1]
    else:
        raise ValueError('Value out of range')


numero = int(input("Ingrese un número: "))
print(function_2(numero))
