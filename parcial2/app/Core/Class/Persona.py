import random
from abc import ABCMeta, abstractmethod


class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        
    def __str__(self):
        return "".format()

class Cliente(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci, ruc=0):
        super().__init__(nombre, apellido, ci)
        self.ruc = ruc        
        self.identificador = random.randint(0, 9) + ci

    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}, ruc: {}, identificador: {}".format(self.nombre, self.apellido, self.ci, self.ruc, self.identificador)

class Empleado(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci, fecha_inicio):
        super().__init__(nombre, apellido, ci)
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return "nombre: {}, apellido: {}, ci: {}, fecha_inicio: {}".format(self.nombre, self.apellido, self.ci, self.fecha_inicio)
