import datetime

class Transporte():
    def __init__(self, fecha_salida, capacidad, precio_por_kg):
       self.fecha_salida = fecha_salida
       self.capacidad = capacidad
       self.precio_por_kg = precio_por_kg
       self.paquetes = []
       self.capacidad_utilizada = 0

    def agregar_paquete(self, paquete):
        if self.capacidad_utilizada+paquete.peso < self.capacidad:
            self.paquetes.append(paquete)
            self.capacidad_utilizada += paquete.peso
            return True
        else:
            return False
           
    def calcular_costo(self):
        return self.capacidad_utilizada * self.precio_por_kg

    def __str__(self):
        return "fecha_salida: {}, capacidad: {}, precio_por_kg: {}, capacidad_utilizada: ".format(self.fecha_salida,
        self.capacidad, self.precio_por_kg, self.capacidad_utilizada)
