import Paquete
import Transporte
import datetime as date


class Empresa:
    def __init__(self):
        pass


    def asignar_embarque(self, paquetes, transporte):
        for paquete in paquetes:
            if transporte.agregar_paquete(paquete):
                print("Paquete agregado")

    def consultar_embarque(self, transporte):
        print("\n Fecha salida: {} - Fecha llegada: {}".format(transporte.fecha_salida.strftime(
            "%a %d/%b/%Y"), transporte.estimar_fecha_entrega().strftime("%a %d/%b/%Y")))

        for paquete in transporte.lista_paquetes:
            print("\t Codigo:{} \t Peso:{}Kg. \t Costo:{}$".format(paquete.codigo, paquete.peso, paquete.calcular_costo(transporte)))
        print("Peso total del embarque: {}Kg.".format(transporte.peso_embarque))



def main():
    fast = Empresa()
    paquetes = [
        Paquete.PaqueteChico(
            peso=1, fecha=date.datetime(2013, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(
            peso=5, fecha=date.datetime(2014, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(
            peso=11, fecha=date.datetime(2013, 12, 31, 21, 51)),
        Paquete.PaqueteMediano(
            peso=3, fecha=date.datetime(2014, 12, 31, 21, 51)),
        Paquete.PaqueteChico(
            peso=1, fecha=date.datetime(2012, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(
            peso=15, fecha=date.datetime(2013, 12, 31, 21, 51)),
    ]

    buque = Transporte.TransporteMaritimo(
        tarifa=9, dias=30, limite=8000, fecha=date.datetime(2018, 6, 1))

    avion = Transporte.TransporteAereo(
        tarifa=22, dias=3, limite=300, fecha=date.datetime(2018, 6, 1))

    fast.asignar_embarque(paquetes, avion)
    fast.consultar_embarque(avion)

main()
