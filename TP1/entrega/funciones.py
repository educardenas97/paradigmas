import random


def function4(n):
    '''Retorna una lista con enteros generados de 1 a N'''
    try:
        if n <= 0:
            raise Exception('Argumento invalido. ')
    except Exception as e:
        print('No es posible generar la lista para ' + str(n))
        raise
    else:
        lista = []
        i = 1
        while i <= n:
            lista.append(i)
            i = i + 1

        return lista


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


def function6(numero):
    ''' Recibe un numero y devuelve una lista con 10 elementos
        correspondientes a la tabla de multiplicar de dicho numero. '''
    try:
        if numero == None:
            raise ValueError
    except Exception as e:
        print('Argumento invalido' + str(e))
        raise
    else:
        lista = []
        for i in range(1, 11):
            lista.append(i*numero)
        return lista


def function7(n, asc=True):
    ''' Recibe un numero n y retorna una lista ordenada generada
        de manera aleatoria. '''
    try:
        if n == None:
            raise ValueError
    except Exception as e:
        print('Argumento no valido' + str(e))
        raise 
    else:
        lista = []
        for i in range(n):
            num_aleatorio = random.randint(0, 9)
            lista.append(num_aleatorio)

        lista.sort(reverse=asc)  # ordena la lista
        return lista


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


def function10(numeros, numero):
    ''' Recibe una lista con numeros y un numero
        devuelve las apariciones de dicho numero en la lista proporcionada. '''
    try:
        if len(numeros) < 1 or numero == None:
            raise ValueError
    except Exception as e:
        raise Exception('Argumento no valido ')
    else:
        contador = 0
        for i in numeros:
            if numero == i:
                contador = contador+1
        return contador


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
        return (minimo, maximo)


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


def function13(regalos):
    ''' Recibe una lista y devuelve una lista con elementos
        seleccionados del argumento seleccionados al azar. '''
    try:
        if len(regalos) < 1:
            raise ValueError
    except Exception as e:
        print('Argumento no valido ' + str(len(regalos)) + str(e))
        raise
    else:
        sorteo_lista = []
        for sorteo in range(5):
            regalo = regalos[random.randint(0, 9)]
            sorteo_lista.append(regalo)

        return sorteo_lista
