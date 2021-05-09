import random
from abc import ABCMeta, abstractmethod


class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        

class Cliente(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci, ruc=0):
        super().__init__(nombre, apellido, ci)
        self.ruc = ruc        
        self.identificador = random.randint(0, 9) + super().ci

class Empleado(Persona):
    '''Especialización de la clase Persona'''
    def __init__(self, nombre, apellido, ci, fecha_inicio):
        super().__init__(nombre, apellido, ci)
        self.fecha_inicio = fecha_inicio
