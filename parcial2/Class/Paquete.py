from abc import ABCMeta, abstractmethod
import random
import datetime
import Transporte


class Paquete(metaclass=ABCMeta):
    '''Clase abstracta de Paquete'''
    cantidad_paquetes = 0

    def __init__(self, identificador, description, peso, fecha):
        self.nombre = nombre
        self.identificador = identificador
        self.peso = peso
        self.fecha_recepcion = fecha
        #Se incrementa la cantidad de instancias
        Paquete.cantidad_paquetes += 1

    def __str__(self):
        '''Genera una cadena con los datos del paquete'''
        return 'Codigo:{},\t Nombre:{}, \t Peso:{}Kg, \t Recepcion:{}'.format(self.codigo,
                                                                              self.nombre, self.peso, self.fecha_recepcion.strftime('%a %d/%b/%Y'))

    @abstractmethod
    def calcular_costo():
        '''Metodo abstracto para calcular el costo segun el tipo
        de paquete'''
        pass

    @staticmethod
    def obtener_total_paquetes():
        '''Metodo estatico que retorna la cantidad de instancias de paquetes'''
        return total_paquetes
