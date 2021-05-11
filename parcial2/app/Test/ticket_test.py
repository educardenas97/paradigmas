import datetime
from app.Core.Class import Empresa
from app.Core.Class import Transporte
from app.Core.Class import Ticket
from app.Core.Class import Persona

empresa = Empresa.Empresa('pepe', '192.168.0.1')
transporte1 = Transporte.Transporte(datetime.datetime.now(), 100, 20)
transporte2 = Transporte.Transporte(datetime.datetime(2021, 12, 13), 100, 20)
empresa.agregar_transporte(transporte2)

empleado = Persona.Empleado('Ed', 'Gomez', 4659680, datetime.datetime.now())
#Se añade a la empresa el empleado
empresa.empleados.append(empleado)
#Se crea un paquete de prueba, 
paquete = empleado.agregar_paquete(300, 1024, 'Cooler Master', 400)

#Ticket
if transporte1.agregar_paquete(paquete):
    ticket = Ticket.TicketRecepcion(datetime.datetime.now(), paquete.calcular_precio(transporte2.precio_por_kg), paquete)
    print("-----------")
    print(ticket)
    print("-----------")
    print(paquete)
    print("-----------")
    print(empresa)
else:
    empresa.paquetes_pendientes.put(paquete)
    print("Cantidad de paquetes_pendientes: {}".format(
        empresa.paquetes_pendientes.qsize()))
