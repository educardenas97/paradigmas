import Paquete
import Transporte


class Empresa:
    def __init__(self):
        self.buque = Transporte.TransporteMaritimo(costo=9, dias=30, limite=8000)
        self.avion = Transporte.TransporteAereo(costo=22, dias=30, limite=300)

        self.paquetes = [
            Paquete.PaqueteChico(1),
            Paquete.PaqueteGrande(5)
        ]

        print("Costo: ", self.paquetes[0].calcular_costo(self.avion))

def main():
    fast = Empresa()

main()
