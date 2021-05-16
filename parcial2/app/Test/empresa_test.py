import datetime
from app.Core.Class import Empresa
from app.Core.Class import Transporte

empresa = Empresa.Empresa('pepe', '192.168.0.1')
transporte1 = Transporte.Transporte(datetime.datetime.now(), 100, 20)
transporte2 = Transporte.Transporte(datetime.datetime(2021,12, 13), 100, 20)
empresa.agregar_transporte(transporte2)
empresa.agregar_transporte(transporte1)

for transporte in empresa.transportes_disponibles:
    print(transporte)
