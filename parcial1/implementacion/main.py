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
    
    try:
        fast.asignar_embarque(paquetes, avion)
    except Exception as e:
        print(e)
    
    fast.consultar_embarque(avion)


main() 
