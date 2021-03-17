from abc import ABCMeta, abstractmethod
import Paquete
import datetime


class Transporte(metaclass=ABCMeta):
    '''Clase abstracta de Transporte'''
    def __init__(self, nombre, fecha, tarifa, dias, limite):
        #Identificador del transporte
        self.nombre = nombre

        self.fecha_salida = fecha
        self.tarifa = tarifa
        self.tiempo_entrega = dias
        self.limite_peso = limite
        self.peso_embarque = 0
        #Lista de paquetes embarcados
        self.lista_paquetes = []

    def agregar_paquete(self, paquete):
        '''Lista de paquetes agregados en espera de salida'''
        #Se retorna un valor true en caso ser exitosa la operación
        if self.peso_embarque+paquete.peso < self.limite_peso:
            self.lista_paquetes.append(paquete)
            self.peso_embarque += paquete.peso
            return True
        else:
            return False

    def estimar_fecha_entrega(self):
        '''Estimación de la posible fecha de entrega'''
        return self.fecha_salida + datetime.timedelta(days=self.tiempo_entrega)
    

class TransporteMaritimo(Transporte):
    '''Especializacion de la clase Transporte'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

class TransporteAereo(Transporte):
    '''Especializacion de la clase Transporte'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
