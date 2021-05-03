from Class import Paquete

from Database import paquetes_persist as db


def registrar_paquete(codigo, peso, descripcion):
    if peso > 10:
        paquete = Paquete.PaqueteChico(peso, codigo, descripcion)
        db.insert(paquete)
        print(paquete.__str__()) 
        print(db.find('Paquete'))
    elif peso > 30:
        paquete = Paquete.PaqueteMediano(peso, codigo, descripcion)
        print('Paquete Creado')
    else:
        paquete = Paquete.PaqueteGrande(peso, codigo, descripcion)
        print('Paquete Creado')


registrar_paquete(98992, 32, "Pepe packa")
