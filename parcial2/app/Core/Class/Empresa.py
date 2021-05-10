class Empresa:
    def __init__(self, razon_social, direccion):
        self.razon_social = razon_social
        self.direccion = direccion
        self.paquetes_pendientes = []
        self.paquetes_entregados = []
        self.transportes_disponibles = []
        self.embarques_realizados = []
        self.empleados = []
        self.clientes = []
    
    def calcular_rentabilidad():
        pass
    
    def __str__(self):
        return "razon_social: {}, direccion: {}, paquetes_pendientes: {}, paquetes_entregados: {}, transportes_disponibles: {}, embarques_realizados: {}, empleados: {}, clientes: {}".format(self.razon_social, 
        self.direccion, self.paquetes_pendientes, self.paquetes_entregados, self.transportes_disponibles, self.embarques_realizados, self.empleados, self.clientes)