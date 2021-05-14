import datetime
from app.Core.Class import *

app = App.App('Front', 'direct')

#Empleados
app.registrar_empleado('pepe', 'gallo', 783)
app.registrar_empleado('Ed', 'Gomez', 4659580)
app.registrar_empleado('pepae', 'gallo', 783234)

#clientes
app.registrar_cliente('Yo', 'Merengues', 4659580, 11290633)
identificador = app.empresa.clientes[0].identificador

#Transportes
app.registrar_transporte(datetime.datetime.now(), 23, 0.1)

#Paquetes
app.registrar_paquete(int(identificador), 43, 'GGG')
app.registrar_paquete(2, 43, 'ttt')
app.registrar_paquete(234, 43, 'GGG')
app.registrar_paquete(2, 43, 'ttt')

#debugging
print(app.empresa)
