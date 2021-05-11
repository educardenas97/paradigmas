from app.Core.Class import Empresa
from app.Core.Class import Paquete
from app.Core.Class import Persona
from app.Core.Class import Ticket
from app.Core.Class import Transporte
from app.Core.Database import Database
import datetime

class App():
    def __init__(self, razon_social, direccion):
        self.empresa = Empresa.Empresa(razon_social, direccion)
        self.db = Database.Database()
        #self.db.insert(self.empresa, 'empresa')
        #Agregar una comprobación en caso de que el sistema se reinicie.

    def registrar_empleado(self, nombre, apellido, ci):
        empleado = Persona.Empleado(nombre, apellido, ci, datetime.datetime.now())
        self.empresa.empleados.append(empleado)
        #self.db.insert(self.empresa, 'empresa')

    def registrar_cliente(self, nombre, apellido, ci, ruc):
        cliente = Persona.Cliente(nombre, apellido, ci, ruc)
        self.empresa.clientes.append(cliente)
        #self.db.insert(self.empresa, 'empresa')

    def registrar_transporte(self, fecha_salida, precio_por_kg, capacidad):
        transporte = Transporte.Transporte(fecha_salida, capacidad, precio_por_kg)
        self.empresa.transportes_disponibles.agregar_transporte(transporte)
        #self.db.insert(self.empresa, 'empresa')

    
    def registrar_paquete(self, codigo, peso, descripcion, valor_articulo=0):
        paquete = self.empresa.empleados[0].agregar_paquete(codigo, peso, descripcion, valor_articulo)

        for transporte in self.empresa.transportes_disponibles:
            if transporte.agregar_paquete(paquete):
                ticket = App.generar_ticket_recepcion(transporte, paquete)
                self.empresa.paquetes_transito.append(ticket)
                #self.db.insert(self.empresa, 'empresa')
                return

        self.empresa.paquetes_pendientes.put(paquete)
        #self.db.insert(self.empresa, 'empresa')

    def generar_ticket_recepcion(transporte, paquete):
        fecha_embarque = transporte.fecha_salida
        costo = paquete.calcular_precio(transporte)
        ticket = Ticket.TicketRecepcion(fecha_embarque, costo, paquete)
        return ticket

    
