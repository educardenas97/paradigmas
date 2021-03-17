import datos
import Paquete
import Transporte
import Empresa
import datetime as date
import time


def main():
    fast = Empresa.Empresa()
    print("------- Paquetes recepcionados ----------")
    paquetes = datos.paquetes()
    for paquete in paquetes:
        print(paquete.__str__())
    print("------------------------------------------")

    buque = datos.transporte("Maritimo")
    avion = datos.transporte("Aereo")

    fast.asignar_embarque(paquetes, avion)
    fast.consultar_embarque(avion)


main() 
