from Class import Paquete

from Database import Database as DB

db = DB.Database('app/Core/Database/Data.fs')

def registrar_paquete(codigo, peso, descripcion):
    if peso > 10:
        paquete = Paquete.PaqueteChico(peso, codigo, descripcion)
        db.insert(paquete, 'Paquete')
        print(db.find('Paquete'))
    elif peso > 30:
        paquete = Paquete.PaqueteMediano(peso, codigo, descripcion)
        print('Paquete Creado')
    else:
        paquete = Paquete.PaqueteGrande(peso, codigo, descripcion)
        print('Paquete Creado')


print(db.find('Paquete'))
