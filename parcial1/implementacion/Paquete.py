from abc import ABCMeta, abstractmethod
import random
import datetime
import Transporte

class Paquete(metaclass=ABCMeta):
    '''Clase abstracta de Paquete'''
    total_paquetes = 0
    
    def __init__(self, nombre, peso, fecha):
        self.nombre = nombre
        self.codigo = random.randint(1, 11)
        self.peso = peso
        self.fecha_recepcion = fecha
        #Se incrementa la cantidad de instancias
        Paquete.total_paquetes += 1

    def __str__(self):
        '''Genera una cadena con los datos del paquete'''
        return 'Codigo:{},\t Nombre:{}, \t Peso:{}, \t Recepcion:{}'.format(self.codigo, self.nombre, self.peso, self.fecha_recepcion.strftime('%a %d/%b/%Y'))

    @abstractmethod
    def calcular_costo():
        '''Metodo abstracto para calcular el costo segun el tipo
        de paquete'''
        pass

    @staticmethod
    def obtener_total_paquetes():
        '''Metodo estatico que retorna la cantidad de instancias de paquetes'''
        return total_paquetes


class PaqueteChico(Paquete):
    '''Clase que representa a los paquetes chicos de entre 0.01 y 1.5kg'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calcular_costo(self, transporte):
        '''Implementacion del metodo abstracto para el calculo del costo
        para los paquetes pequeños'''
        return self.peso * transporte.tarifa


class PaqueteMediano(Paquete):
    '''Clase que representa a los paquetes medianos de entre 1.5 y 4kg'''
    descuento = 0.03

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calcular_costo(self, transporte):
        '''Implementacion del metodo abstracto para el calculo del costo
        para los paquetes medianos'''
        total = self.peso * transporte.tarifa
        neto = total - (total * PaqueteMediano.descuento)
        return neto
    

class PaqueteGrande(Paquete):
    '''Clase que representa a los paquetes grandes de 4kg en adelante'''
    descuento = 0.05

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calcular_costo(self, transporte):
        '''Implementacion del metodo abstracto para el calculo del costo
        para los paquetes grandes'''
        total = self.peso * transporte.tarifa
        neto = total - (total * PaqueteGrande.descuento)
        return neto
