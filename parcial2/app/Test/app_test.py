from app.Core.Class import *

app = App.App('Front', 'direct')
app.registrar_empleado('pepe', 'gallo', 783)
app.registrar_empleado('Ed', 'Gomez', 4659580)
app.registrar_empleado('pepae', 'gallo', 783234)

app.registrar_paquete(234, 43, 'GGG')
print(app.empresa)