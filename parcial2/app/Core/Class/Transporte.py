class Transporte():
    def __init__(self, fecha_salida, capacidad, precio_por_kg, fecha_llegada):
       self.fecha_salida = fecha_salida
       self.fecha_llegada = fecha_llegada
       self.capacidad = capacidad
       self.precio_por_kg = precio_por_kg
       self.paquetes = []
       self.capacidad_utilizada = Transporte.sumar_paquetes(self.paquetes)
       self.capacidad_disponible = capacidad - self.capacidad_utilizada

    def sumar_paquetes(paquetes):
        total = 0
        for paquete in paquetes:
            total += paquete.peso
        return total

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
        return "fecha_salida: {}, fecha_llegada: {}, capacidad: {}, precio_por_kg: {}, capacidad_utilizada: ".format(self.fecha_salida, self.fecha_llegada,
        self.capacidad, self.precio_por_kg, self.capacidad_utilizada)
