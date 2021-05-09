from . import Empresa
from . import Paquete
from . import Persona
from . import Ticket
from . import Transporte
from app.Core.Database import Database

class App():
    def __init__(self, razon_social, direccion):
        self.empresa = Empresa.Empresa(razon_social, direccion)

    def agregar_paquete(codigo, peso, descripcion, impuesto=0, valor_articulo=0):
        pass
