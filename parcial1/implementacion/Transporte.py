from abc import ABCMeta, abstractmethod
import Paquete

class Transporte():
    def __init__(self, costo, dias, limite):
        self.costo = costo
        self.tiempo_entrega = dias
        self.limite_peso = limite
        self.lista_paquetes = []

    def agregar_paquete(paquete):
        self.lista_paquetes.append(paquete)

    

class TransporteMaritimo(Transporte):
    def __init__(self, costo, dias, limite):
        Transporte.__init__(self, costo, dias, limite)
        print("Transporte maritimo listo")
    

class TransporteAereo(Transporte):
    def __init__(self, costo, dias, limite):
        Transporte.__init__(self, costo, dias, limite)
        print("Transporte aereo listo")
