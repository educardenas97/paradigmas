#!/usr/bin/python3

def function9(cadena):
    ''' Recibe una cadena y devuelve la misma cadena con
        los caracteres repetidos eliminados. '''
    try:
        if len(cadena) < 1:
            raise ValueError(str(len(cadena)))
    except Exception as e:
        print('Argumento invalido: longitud de cadena ' + str(e))
        raise 
    else:        
        lista = []
        for c in cadena:
            if c not in lista:
                lista.append(c)
                
        return "".join(map(str, lista))


def main():
    try:
        ''' Se solicita una cadena y se llama a
            function9 para mostrar el resultado  '''
        cadena = input("Ingrese una cadena: ")
        print(function9(cadena))
    except Exception as e:
        print('Ha ocurrido un error ')
