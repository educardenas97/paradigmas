from app.View.administracion import main as administracion
from app.View.paqueteria import main as paqueteria
from app.View.transportes import main as transportes
from app.View.funciones import *

def main():
    items = ["Administracion", "Paquetería", "Transporte", "Salir"]
    secciones = [administracion, paqueteria, transportes]

    options = sub_menu(items, "Menu Principal")
    while options != len(items):
        if options == len(items):
            print("Exit()")
            exit()
        elif options != len(items):
            secciones[options-1]()
        else:
            print("Opcion no permitida")

        options = sub_menu(items, "Menu Principal")

main()
