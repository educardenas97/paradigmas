from abc import ABCMeta, abstractmethod
import random
import Transporte

class Paquete(metaclass=ABCMeta):
    def __init__(self, peso):
        self.codigo = random.randint(0, 9)
        self.peso = peso

    @abstractmethod
    def calcular_costo():
        pass

class PaqueteChico(Paquete):
    def __init__(self, peso):
        Paquete.__init__(self,peso)
    
    def calcular_costo(self, transporte):
        return self.peso * transporte.costo


class PaqueteMediano(Paquete):
    def __init__(self, peso):
        descuento = 0.03
        Paquete.__init__(self,peso)

    def calcular_costo(self, transporte):
        total = self.peso * transporte.costo
        neto = total - (total*descuento)
        return neto
    

class PaqueteGrande(Paquete):
    def __init__(self, peso):
        descuento = 0.05
        Paquete.__init__(self,peso)

    def calcular_costo(self, transporte):
        total = self.peso * transporte.costo
        neto = total - (total*descuento)
        return neto
