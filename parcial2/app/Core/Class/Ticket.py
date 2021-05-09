from abc import ABCMeta, abstractmethod

class Ticket(metaclass=ABCMeta):
    def __init__(self, peso, fecha, costo):
        self.peso = peso
        self.fecha = fecha
        self.costo = costo
    
    @abstractmethod
    def imprimir_ticket():
        pass

    def __str__(self):
        return "peso: {}, fecha: {}, costo:{}".format(self.peso, self.fecha, self.costo)

class TicketRecepcion(Ticket):
    def __init__(self, peso, fecha, costo, paquete, empleado):
        super().__init__(peso, fecha, costo)
        self.paquete = paquete
        self.empleado = empleado
        self.fecha_embarque = fecha_embarque

    def imprimir_ticket(self):
        return {
            "peso": self.peso,
            "fecha": self.fecha,
            "precio": self.costo,
            "paquete": {
                "codigo": self.paquete.codigo, 
                "peso": self.paquete.peso,
            },
            "empleado": {
                "apellido": self.empleado.apellido, 
                "nombre": self.empleado.nombre,
            },
            "fecha_embarque": self.fecha_embarque
        }
    
    def __str__(self):
        return "{}, paquete: {}, empleado: {}, fecha_embarque: {}".format(self.super(), self.paquete, self.empleado, self.fecha_embarque)

class TicketEmbarque(Ticket):
    def __init__(self, peso, fecha, costo, transporte):
        super().__init__(peso, fecha, costo)
        self.transporte = transporte

    def imprimir_ticket():
        return{
            "peso": self.peso,
            "fecha_salida": self.fecha,
            "costo": self.costo,
            "transporte": self.transporte
        }

    def __str__(self):
        return "{}, transporte: {}".format(self.super(), self.transporte)