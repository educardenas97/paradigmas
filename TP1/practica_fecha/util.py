import datetime
def es_fecha_valida(str_fecha, lanzar_excepcion=False):
   """Valida la fecha en el formato 'dd/mm/aaaa' lanzando o no una excepción. 
      Se requiere la importación previa del módulo 'datetime'.

      Parámetros:
         str_fecha (cadena): La fecha como cadena 'dd/mm/aaaa'.
            lanzar_excepcion (lógico): Especifica si se debe lanzar o no una 
            excepción. Por defecto es falso.

      Retorna:
         (lógico): Verdadero en caso de fecha válida y Falso en caso contrario. 

   """
   try:
      obj_fecha = datetime.datetime.strptime(str_fecha, '%d/%m/%Y')
      return True
   except ValueError:
      if lanzar_excepcion:
         raise Exception("Fecha incorrecta para el formato 'dd/mm/aaaa'.")
      else:
         return False


def leer_fecha(nro_intentos=3):
   for k in range(nro_intentos): 
      fecha = input('Ingrese una fecha [dd/mm/aaaa]: ')
      if es_fecha_valida(fecha):
         return fecha
   return None
   
     


