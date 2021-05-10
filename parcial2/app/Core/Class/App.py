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
        self.db.insert(self.empresa, 'empresa')
        #Agregar una comprobación en caso de que el sistema se reinicie.

    def registrar_empleado(self, nombre, apellido, ci):
        empleado = Persona.Empleado(nombre, apellido, ci, datetime.datetime.now())
        self.empresa = self.db.find('empresa')
        self.empresa.empleados.append(empleado)
        self.db.insert(self.empresa, 'empresa')