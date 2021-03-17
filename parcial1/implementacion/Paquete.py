from abc import ABCMeta, abstractmethod
import random
import Transporte

class Paquete(metaclass=ABCMeta):
    ''' Clase abstracta de Paquete '''
    total_paquetes = 0
    
    def __init__(self, peso):
        self.codigo = random.randint(0, 9)
        self.peso = peso
        #Se incrementa la cantidad de instancias
        Paquete.total_paquetes += 1

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
        return self.peso * transporte.tarifa


class PaqueteMediano(Paquete):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        descuento = 0.03

    def calcular_costo(self, transporte):
        total = self.peso * transporte.tarifa
        neto = total - (total*descuento)
        return neto
    

class PaqueteGrande(Paquete):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        descuento = 0.05

    def calcular_costo(self, transporte):
        total = self.peso * transporte.tarifa
        neto = total - (total*descuento)
        return neto
