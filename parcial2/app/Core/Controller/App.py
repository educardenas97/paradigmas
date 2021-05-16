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
        return self.empresa.empleados

    def registrar_cliente(self, nombre, apellido, ci, ruc):
        cliente = Persona.Cliente(nombre, apellido, ci, ruc)
        self.empresa.clientes.append(cliente)
        #self.db.insert(self.empresa, 'empresa')
        return self.empresa.clientes

    def registrar_transporte(self, fecha_salida, precio_por_kg, capacidad, fecha_llegada=0):
        fecha_llegada = fecha_salida + datetime.timedelta(days=4) if fecha_llegada == 0 else fecha_llegada
        transporte = Transporte.Transporte(fecha_salida, capacidad, precio_por_kg, fecha_llegada)
        self.empresa.agregar_transporte(transporte)
        while self.empresa.paquetes_pendientes.qsize() != 0:
            paquete_pendiente = self.empresa.paquetes_pendientes.get()
            if not transporte.agregar_paquete(paquete_pendiente):
                self.empresa.paquetes_pendientes.put(paquete_pendiente)
            else:
                cliente = App.determinar_cliente(self.empresa.clientes, paquete_pendiente)
                ticket = App.generar_ticket_recepcion(transporte, paquete_pendiente, cliente)
                self.empresa.paquetes_transito.append(ticket)

        #self.db.insert(self.empresa, 'empresa')
        return self.empresa.transportes_disponibles
    
    def registrar_paquete(self, codigo, peso, descripcion, valor_articulo=0):
        paquete = App.agregar_paquete(codigo, peso, descripcion, valor_articulo)

        for transporte in self.empresa.transportes_disponibles:
            if transporte.agregar_paquete(paquete):
                cliente = App.determinar_cliente(self.empresa.clientes, paquete)
                ticket = App.generar_ticket_recepcion(transporte, paquete, cliente)
                self.empresa.paquetes_transito.append(ticket)
                #self.db.insert(self.empresa, 'empresa')
                return ticket

        self.empresa.paquetes_pendientes.put(paquete)
        #self.db.insert(self.empresa, 'empresa')
        return self.empresa.paquetes_pendientes.qsize()

    def generar_ticket_recepcion(transporte, paquete, cliente):
        fecha_embarque = transporte.fecha_salida
        costo = paquete.calcular_precio(transporte.precio_por_kg)
        ticket = Ticket.TicketRecepcion(fecha_embarque, costo, paquete, cliente)
        return ticket

    def determinar_cliente(clientes, paquete):
        for cliente in clientes:
            if cliente.identificador == paquete.codigo:
                return cliente
        
        return Persona.Cliente('Desconocido', 'Desconocido')

    def agregar_paquete(codigo, peso,  descripcion, valor_articulo=0):
        if peso > 0 and peso <= 100:
            return Paquete.PaqueteChico(peso, codigo, descripcion)
        elif peso > 100 and peso <= 2000:
            return Paquete.PaqueteMediano(peso, codigo, descripcion)
        elif peso > 2000 and valor_articulo != 0:
            return Paquete.PaqueteGrande(peso, codigo, descripcion, valor_articulo)
        else:
            raise ValueError('valor_articulo: {}'.format(valor_articulo))
        
