from abc import ABCMeta, abstractmethod

class Paquete(metaclass=ABCMeta):
    def __init__(self, peso, codigo, descripcion):
        self.peso = peso/1000
        self.codigo = codigo
        self.descripcion = descripcion

    @abstractmethod
    def calcular_precio():
        pass

    def __str__(self):
        return "codigo: {}, peso: {}, descripcion: {}".format(self.codigo, self.peso, self.descripcion)


class PaqueteChico(Paquete):
    margen_ganancia = 12 #porcentual

    def __init__(self, peso, codigo, descripcion):
        super().__init__(peso, codigo, descripcion)

    def calcular_precio(self, transporte):
        costo = transporte.costo_por_kg * self.peso
        total = costo * (PaqueteChico.margen_ganancia/100) + 1
        return total

    def __str__(self):
        return "PaqueteChico: \n {}".format(super().__str__())
   
class PaqueteMediano(Paquete):
    margen_ganancia = 10 #porcentual

    def __init__(self, peso, codigo, descripcion, impuesto=3):
        super().__init__(peso, codigo, descripcion)
        self.impuesto = impuesto

    def calcular_precio(self, transporte):
        costo = transporte.costo_por_kg * self.peso
        precio_sin_impuesto = costo * ((PaqueteMediano.margen_ganancia/100) + 1)
        total = precio_sin_impuesto * ((self.impuesto/100) + 1)
        return total

    def __str__(self):
        return "PaqueteMediano: \n {}".format(super().__str__())

class PaqueteGrande(Paquete):
    margen_ganancia = 5  # porcentual

    def __init__(self, peso, codigo, descripcion, valor_articulo, impuesto=8):
        super().__init__(peso, codigo, descripcion)
        self.impuesto = impuesto
        self.valor_articulo = valor_articulo

    def calcular_precio(self, transporte):
        costo = transporte.costo_por_kg * self.peso
        precio_sin_impuesto = costo * ((PaqueteGrande.margen_ganancia/100) + 1)
        impuesto_a_pagar = self.valor_articulo  * ((self.impuesto/100) + 1)
        total = precio_sin_impuesto + impuesto_a_pagar
        return total

    def __str__(self):
        return "PaqueteGrande: \n {}".format(super().__str__())
