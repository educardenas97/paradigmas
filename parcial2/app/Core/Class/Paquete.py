from abc import ABCMeta, abstractmethod

class Paquete(metaclass=ABCMeta):
    def __init__(self, peso, codigo, descripcion):
        self.peso = peso
        self.codigo = codigo
        self.descripcion = descripcion

    @abstractmethod
    def calcular_precio():
        pass


class PaqueteChico(Paquete):
    def __init__(self, peso, codigo, descripcion):
        super().__init__(peso, codigo, descripcion)

    def calcular_precio(self, costo_por_kg):
        return self.peso * costo_por_kg

    def __str__(self):
        return "peso: {}, descripcion: {}".format(self.peso, self.descripcion)

class PaqueteMediano(Paquete):
    def __init__(self, peso, codigo, descripcion, impuesto):
        super().__init__(peso, codigo, descripcion)
        self.impuesto = impuesto

    def calcular_precio(self, costo_por_kg):
        return (self.peso * costo_por_kg) + self.impuesto

class PaqueteGrande(Paquete):
    def __init__(self, peso, codigo, descripcion, impuesto, valor_articulo):
        super().__init__(peso, codigo, descripcion)
        self.impuesto = impuesto
        self.valor_articulo = valor_articulo

    def calcular_precio(self, costo_por_kg):
        return (self.peso * costo_por_kg) + self.impuesto + (valor_articulo*0.3)
