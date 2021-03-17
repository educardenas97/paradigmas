from abc import ABCMeta, abstractmethod
import Paquete
import datetime

class Transporte():
    def __init__(self, fecha, tarifa, dias, limite):
        self.fecha_salida = fecha
        self.tarifa = tarifa
        self.tiempo_entrega = dias
        self.limite_peso = limite

        self.peso_embarque = 0
        self.lista_paquetes = []

    def agregar_paquete(self, paquete):
        '''Lista de paquetes agregados en espera de salida'''
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Transporte maritimo listo")
    

class TransporteAereo(Transporte):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Transporte aereo listo")
