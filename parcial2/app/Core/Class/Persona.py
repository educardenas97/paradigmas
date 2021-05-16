import random

class Persona():
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        
    def __str__(self):
        return "".format()

class Cliente():
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci=0, ruc=0):
        self.persona = Persona(nombre, apellido, ci)
        self.ruc = ruc        
        self.identificador = (random.randint(0, 9) + ci) if ci != 0 else 0

    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}, ruc: {}, identificador: {}".format(self.persona.nombre, self.persona.apellido, self.persona.ci, self.ruc, self.identificador)

class Empleado(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci, fecha_inicio):
        self.persona = Persona(nombre, apellido, ci)
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}, fecha_inicio: {}".format(self.persona.nombre, self.persona.apellido, self.persona.ci, self.fecha_inicio)
