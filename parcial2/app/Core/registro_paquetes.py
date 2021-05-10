from Class import Paquete
from Class import Ticket
from Class import Transporte

from Database import Database as DB

db = DB.Database('app/Core/Database/Data.fs')

def registrar_paquete(codigo, peso, descripcion, impuesto=0, valor_articulo=0):
    if peso > 10:
        paquete = Paquete.PaqueteChico(peso, codigo, descripcion)
        db.insert(paquete)
        print(db.find(paquete))
    elif peso > 30:
        paquete = Paquete.PaqueteMediano(peso, codigo, descripcion)
        print('Paquete Creado')
    else:
        paquete = Paquete.PaqueteGrande(peso, codigo, descripcion, impuesto, valor_articulo)
        print('Paquete Creado')


def generar_ticket(paquete, transporte):
    pass

registrar_paquete(3203923, 2, "Paquete, pepe")