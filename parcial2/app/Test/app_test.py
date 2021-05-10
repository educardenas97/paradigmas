import unittest
from app.Core.Class import *
from app.Core.Database import *

app = App.App('Front', 'direct')
app.registrar_empleado('pepe', 'gallo', 783)
app.registrar_empleado('Ed', 'Gomez', 4659580)
app.registrar_empleado('pepae', 'gallo', 783234)

#test de persistencia
print(app.db.find('empresa'))
