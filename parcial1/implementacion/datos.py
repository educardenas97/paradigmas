import Paquete
import Transporte
import datetime as date

def paquetes():
    return [
        Paquete.PaqueteChico(nombre = "Intel i9",
            peso=1, fecha=date.datetime(2013, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(nombre = "Gabinete CM",
            peso=5, fecha=date.datetime(2014, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(nombre = "Monitor",
            peso=11, fecha=date.datetime(2013, 12, 31, 21, 51)),
        Paquete.PaqueteMediano(nombre = "Noctua PPC",
            peso=3, fecha=date.datetime(2014, 12, 31, 21, 51)),
        Paquete.PaqueteChico(nombre = "RAM Kingston",
            peso=1, fecha=date.datetime(2012, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(nombre = "Monitor",
            peso=15, fecha=date.datetime(2013, 12, 31, 21, 51)),
        Paquete.PaqueteChico(nombre = "AMD Ryzen 3",
            peso=1, fecha=date.datetime(2013, 12, 31, 21, 51)),
        Paquete.PaqueteGrande(nombre = "Pantalla",
            peso=15, fecha=date.datetime(2014, 12, 31, 21, 51)),
    ]

def transporte(tipo):
    if tipo == "Maritimo":
        return Transporte.TransporteMaritimo(nombre="Buque 091",
            tarifa=9, dias=30, limite=2000, fecha=date.datetime(2018, 6, 1))
    if tipo == "Aereo":
        return Transporte.TransporteAereo(nombre="Boing 766",
            tarifa=22, dias=3, limite=300, fecha=date.datetime(2018, 6, 1))
