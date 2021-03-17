import Paquete
import Transporte
import datetime as date
import time
import sys

class Empresa:
    '''Clase Empresa, no se requieren parametros para instanciarla'''
    def __init__(self):
        pass

    def asignar_embarque(self, paquetes, transporte):
        #breve animacion de carga
        animation = "|/-\\"
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        #se asignan paquetes al transporte
        for paquete in paquetes:
            transporte.agregar_paquete(paquete)

    def consultar_embarque(self, transporte):
        print("\n----------Ticket de embarco--------")
        print("Transporte: {}".format(transporte.nombre))
        print("Fecha salida: {} \nFecha llegada: {}".format(transporte.fecha_salida.strftime(
            "%a %d/%b/%Y"), transporte.estimar_fecha_entrega().strftime("%a %d/%b/%Y")))
        print("Carga a bordo: ")
        for paquete in transporte.lista_paquetes:
            print("\t Codigo:{} \t Peso:{}Kg. \t Costo:{}$"
            .format(paquete.codigo, paquete.peso, paquete.calcular_costo(transporte)))
        print("Total de paquetes: {}".format(len(transporte.lista_paquetes)))
        print("Capacidad de carga: {}Kg.".format(transporte.limite_peso))
        print("Peso total del embarque: {}Kg.".format(transporte.peso_embarque))
        print("Aprovechamiento de la capacidad de carga: {:.2f}%"
            .format((transporte.peso_embarque/transporte.limite_peso)*100))
        print("----------------------------------")


