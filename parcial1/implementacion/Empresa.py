import Paquete
import Transporte
import datetime


class Empresa:
    def __init__(self):
        self.buque = Transporte.TransporteMaritimo(
            tarifa=9, dias=30, limite=8000, fecha=datetime.datetime(2018, 6, 1))

        self.avion = Transporte.TransporteAereo(
            tarifa=22, dias=30, limite=300, fecha=datetime.datetime(2018, 6, 1))

        self.paquetes = [
            Paquete.PaqueteChico(peso=1),
            Paquete.PaqueteGrande(peso=5)
        ]

        print("Costo: ", self.paquetes[0].calcular_costo(self.avion), "Kg:", self.paquetes[0].peso)

def main():
    fast = Empresa()

main()
