from abc import ABCMeta, abstractmethod
import Paquete
import datetime

class Transporte():
    def __init__(self, fecha, tarifa, dias, limite):
        self.fecha_salida = fecha
        self.tarifa = tarifa
        self.tiempo_entrega = dias
        self.limite_peso = limite
        self.lista_paquetes = []

    def agregar_paquete(paquete):
        self.lista_paquetes.append(paquete)

    

class TransporteMaritimo(Transporte):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Transporte maritimo listo")
    

class TransporteAereo(Transporte):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Transporte aereo listo")
