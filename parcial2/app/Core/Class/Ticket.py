from abc import ABCMeta, abstractmethod
class Ticket(metaclass=ABCMeta):
    def __init__(self, peso, fecha, costo):
        self.peso = peso
        self.fecha = fecha
        self.costo = costo
    
    @abstractmethod
    def imprimir_ticket():
        pass

class TicketRecepcion(Ticket):
    def __init__(self, peso, fecha, costo, paquete, empleado, fecha_embarque):
        super().__init__(peso, fecha, costo)
        self.paquete = paquete
        self.empleado = empleado
        self.fecha_embarque = fecha_embarque

    def imprimir_ticket(self):
        pass