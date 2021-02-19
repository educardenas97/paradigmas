#!/usr/bin/python3
from util import leer_fecha

def iniciar_principal():
   # Solicitamos una fecha al usuario:
   fecha_solicitada = leer_fecha()
   # Imprimimos la fecha leída.
   print('La fecha ingresada es: ', fecha_solicitada)


if __name__ == "__main__":
   iniciar_principal()
