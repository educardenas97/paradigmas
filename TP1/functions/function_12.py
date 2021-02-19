#!/usr/bin/python3

def function_12(cadena):
    cadena_al_reves = cadena[::-1]

    if cadena == cadena_al_reves:
        return True
    else:
        return False


cadena1 = input("Ingrese una cadena: ")
print(function_12(cadena1))
