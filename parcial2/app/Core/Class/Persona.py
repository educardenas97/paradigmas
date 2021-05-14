import random
from abc import ABCMeta, abstractmethod
from . import Paquete

class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        
    def __str__(self):
        return "".format()

class Cliente(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci=0, ruc=0):
        super().__init__(nombre, apellido, ci)
        self.ruc = ruc        
        self.identificador = (random.randint(0, 9) + ci) if ci != 0 else 0

    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}, ruc: {}, identificador: {}".format(self.nombre, self.apellido, self.ci, self.ruc, self.identificador)

class Empleado(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci, fecha_inicio):
        super().__init__(nombre, apellido, ci)
        self.fecha_inicio = fecha_inicio

    def agregar_paquete(self, codigo, peso,  descripcion, valor_articulo=0):
        if peso > 0 and peso <= 100:
            return Paquete.PaqueteChico(peso, codigo, descripcion)
        elif peso > 100 and peso <= 2000:
            return Paquete.PaqueteMediano(peso, codigo, descripcion)
        elif peso > 2000 and valor_articulo != 0:
            return Paquete.PaqueteGrande(peso, codigo, descripcion, valor_articulo)
        else:
            raise ValueError('valor_articulo: {}'.format(valor_articulo))
            return False

    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}, fecha_inicio: {}".format(self.nombre, self.apellido, self.ci, self.fecha_inicio)
